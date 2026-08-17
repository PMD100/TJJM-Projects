# -*- coding: utf-8 -*-
"""Simulate BOTH rendering surfaces over the real corpus, before and after the city
override, using each surface's own parsing semantics."""
import json,os,re,collections
ROOT="/sessions/youthful-gracious-mccarthy/mnt/TJJM Projects"
O=ROOT+'/build-b50b/orig'; B=ROOT+'/build-b50b/built'
NLC=["St. John's","Corner Brook","Gander","Paradise","Conception Bay South",
     "Labrador City","Grand Falls-Windsor","Clarenville","Mount Pearl","Torbay","Flat Bay"]

# ---- rendered output of the cities snippet: Liquid drops {%- comment -%} blocks ----
raw=open(B+'/tjjm-gym-cities.liquid',encoding='utf-8').read()
rendered=re.sub(r'\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}','',raw,flags=re.S)
assert 'comment' not in rendered
print('rendered snippet bytes:',len(rendered.encode('utf-8')),' rows:',rendered.count('~')//2)

# ---- surface B (flat page, JS): overrides() regex, verbatim ----
cov={}
for m in re.finditer(r'~([^|~]*)\|([^~]*)~', rendered):
    cov[m.group(1).strip()]=m.group(2).strip()
print('JS overrides() parsed rows:',len(cov))
assert len(cov)==21, cov

# ---- surface A (region pages, Liquid): contains / split / last / split '~' / first ----
def liquid_probe(name, s):
    p='~'+name+'|'
    if p not in s: return None
    return s.split(p)[-1].split('~')[0].strip()
lq={}
for n in cov:
    lq[n]=liquid_probe(n,rendered)
mismatch={n:(lq[n],cov[n]) for n in cov if lq[n]!=cov[n]}
print('Liquid-vs-JS extraction mismatches:',mismatch or 'NONE')
assert not mismatch

# ---- corpus ----
def parse(p):
    s=open(p,encoding='utf-8').read(); out=[]
    for ch in s.split('{"n":"')[1:]:
        e=ch.find('}')
        if e<0: continue
        try: out.append(json.loads('{"n":"'+ch[:e+1]))
        except Exception: pass
    return out
files=sorted([f for f in os.listdir(O) if re.fullmatch(r'tjjm-gyms-data(-\d+)?\.liquid',f)])
recs=[]
for f in files:
    for r in parse(O+'/'+f): r['_f']=f; recs.append(r)
rem=collections.defaultdict(set)
for line in open(O+'/tjjm-removed-index.liquid',encoding='utf-8'):
    l=line.strip()
    if not l or '|' not in l or l.startswith('{%'): continue
    p=l.split('|'); code=p[0].strip()
    if not re.fullmatch(r'[A-Z]{2}',code): continue
    for n in p[1:]:
        n=n.strip()
        if n: rem[code].add(n)

def run(use_override, surface):
    out=[]
    for r in recs:
        n=(r.get('n') or '').strip()
        if not n: continue
        s=(r.get('s') or '').strip(); c=(r.get('c') or '').strip()
        if n in rem.get(s,()): continue
        # --- region bucketing reads the STORED city on both surfaces ---
        code='NL' if (s=='NE' and c in NLC) else s
        if use_override and n in cov: c=cov[n]     # applied AFTER the NE/NL test
        out.append((n,c,code))
    return out

for surf in ('region-pages','flat-page'):
    before=run(False,surf); after=run(True,surf)
    assert len(before)==len(after)==5215, (len(before),len(after))
    cb=collections.Counter(x[2] for x in before); ca=collections.Counter(x[2] for x in after)
    assert cb==ca, 'REGION COUNTS CHANGED'
    changed=[(b[0],b[1],a[1],b[2]) for b,a in zip(before,after) if b[1]!=a[1]]
    movedreg=[(b[0],b[2],a[2]) for b,a in zip(before,after) if b[2]!=a[2]]
    print('\n== %s ==' % surf)
    print('  published: %d   regions: %d   region counts identical: %s' % (len(after),len(ca),cb==ca))
    print('  records that CHANGED REGION: %d %s' % (len(movedreg), movedreg or ''))
    print('  records whose displayed city changed: %d' % len(changed))
    for x in changed: print('     %-42s %s  %-24s -> %s' % (x[0],x[3],x[1],x[2]))
    noop=[n for n in cov if n not in {x[0] for x in changed}]
    print('  override rows that were a NO-OP (value already correct): %s' % (noop or 'none'))
    json.dump(sorted(ca.items()),open(ROOT+'/build-b50b/region-counts-after.json','w'),indent=0)

# region counts before file must equal after
bef=json.load(open(ROOT+'/build-b50b/region-counts-before.json'))
aft=dict(json.load(open(ROOT+'/build-b50b/region-counts-after.json')))
print('\nregion-counts-before == region-counts-after :', {k:v for k,v in bef.items()}==aft)
