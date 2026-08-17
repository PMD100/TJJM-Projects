import json, os, re, sys, collections
ROOT = "/sessions/youthful-gracious-mccarthy/mnt/TJJM Projects"
ORIG = os.path.join(ROOT, 'build-b50b/orig')

def parse_file(path):
    s = open(path, encoding='utf-8').read()
    out = []
    for chunk in s.split('{"n":"')[1:]:
        end = chunk.find('}')
        if end < 0: continue
        try: r = json.loads('{"n":"' + chunk[:end+1])
        except Exception: continue
        out.append(r)
    return out

files = sorted([f for f in os.listdir(ORIG) if re.fullmatch(r'tjjm-gyms-data(-\d+)?\.liquid', f)],
               key=lambda f: int(re.search(r'-(\d+)\.', f).group(1)) if re.search(r'-(\d+)\.', f) else 0)
assert len(files) == 45, len(files)
recs = []
for f in files:
    for r in parse_file(os.path.join(ORIG, f)):
        r['_file'] = f; recs.append(r)
print('TOTAL RECORDS PARSED:', len(recs))

rem = collections.defaultdict(set)
for line in open(os.path.join(ORIG,'tjjm-removed-index.liquid'), encoding='utf-8'):
    l = line.strip()
    if not l or '|' not in l or l.startswith('{%'): continue
    p = l.split('|'); code = p[0].strip()
    if not re.fullmatch(r'[A-Z]{2}', code): continue
    for n in p[1:]:
        n = n.strip()
        if n: rem[code].add(n)

NLC = ["St. John's","Corner Brook","Gander","Paradise","Conception Bay South",
       "Labrador City","Grand Falls-Windsor","Clarenville","Mount Pearl","Torbay","Flat Bay"]

pub = []
for r in recs:
    n=(r.get('n') or '').strip(); s=(r.get('s') or '').strip(); c=(r.get('c') or '').strip()
    if not n: continue
    if n in rem.get(s, ()): continue
    pub.append((n, c, ('NL' if (s=='NE' and c in NLC) else s), s, r['_file']))
print('PUBLISHED:', len(pub))
regions = collections.Counter(code for _,_,code,_,_ in pub)
print('REGIONS:', len(regions))

byname = collections.defaultdict(list)
for r in recs: byname[(r.get('n') or '').strip()].append(r)
dupes = {k:v for k,v in byname.items() if len(v)>1}
print('DUPLICATED NAMES:', len(dupes), 'surplus:', sum(len(v)-1 for v in dupes.values()))

rows=[l.rstrip('\n').split('\t') for l in open(os.path.join(ROOT,'scratch/identity/apply-b50-city.tsv'), encoding='utf-8') if l.strip()]
hdr=rows[0]; data=rows[1:]; ci={h:i for i,h in enumerate(hdr)}
print('\nTSV data rows:', len(data))
ok=[]; bad=[]
for row in data:
    name=row[ci['name']]; reg=row[ci['region']]; rc=row[ci['record_city']]; nc=row[ci['new_city']]
    m=byname.get(name,[]); st=[]
    if len(m)!=1: st.append(f'MATCHES={len(m)}')
    if '|' in name or '~' in name: st.append('C5-FAIL-NAME')
    if '|' in nc or '~' in nc: st.append('C5-FAIL-VALUE')
    if not nc.strip(): st.append('EMPTY-VALUE')
    if nc in NLC: st.append('NL-CITY-VALUE')
    if len(m)==1:
        r=m[0]
        if (r.get('s') or '').strip()!=reg: st.append(f"REGION-MISMATCH(rec={r.get('s')})")
        if (r.get('c') or '').strip()!=rc: st.append(f"CITY-MISMATCH(rec={r.get('c')})")
        pubnames = {x[0] for x in pub}
        if name not in pubnames: st.append('NOT-PUBLISHED(suppressed)')
    print(f"  {'OK' if not st else 'XX'}  {name:42s} {reg}  {rc:24s} -> {nc:18s} file={(m[0]['_file'] if len(m)==1 else '-'):24s} {';'.join(st)}")
    (ok if not st else bad).append((name,nc,';'.join(st)))
print(f'\nGATE exactly-one-record: {len(ok)} clean, {len(bad)} flagged')
json.dump([[n,c] for n,c,_ in ok], open(os.path.join(ROOT,'build-b50b/city-rows.json'),'w'), indent=1)
json.dump({k:v for k,v in sorted(regions.items())}, open(os.path.join(ROOT,'build-b50b/region-counts-before.json'),'w'), indent=0)
