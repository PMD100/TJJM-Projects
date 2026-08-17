import json, csv, os, sys, hashlib, collections, difflib

BASE="/sessions/youthful-gracious-mccarthy/mnt/TJJM Projects/build-b50"
ORIG=os.path.join(BASE,"orig"); BUILT=os.path.join(BASE,"built"); DIFFS=os.path.join(BASE,"diffs")

def recs_with_raw(txt):
    out=[]; parts=txt.split('{"n":"')
    for chunk in parts[1:]:
        end=chunk.find('}')
        raw='{"n":"'+chunk[:end+1]
        out.append((json.loads(raw), raw))
    return out

TSV="/sessions/youthful-gracious-mccarthy/mnt/TJJM Projects/scratch/identity/apply-b50-city.tsv"
rows=[{k:v.strip() for k,v in r.items()} for r in csv.DictReader(open(TSV,encoding='utf-8-sig'),delimiter='\t')]
assert len(rows)==21, len(rows)

# locate each edit
byfile=collections.defaultdict(list)
allfiles=["tjjm-gyms-data.liquid"]+[f"tjjm-gyms-data-{i}.liquid" for i in range(2,46)]
index={}
for fn in allfiles:
    txt=open(os.path.join(ORIG,fn),encoding='utf-8').read()
    for obj,raw in recs_with_raw(txt):
        index.setdefault((obj['n'],obj.get('c','')),[]).append((fn,obj,raw))

for r in rows:
    key=(r['name'],r['record_city'])
    hits=index.get(key,[])
    assert len(hits)==1, f"NOT UNIQUE {key}: {len(hits)}"
    fn,obj,raw=hits[0]
    assert obj['s']==r['region'], f"region mismatch {key}"
    byfile[fn].append((r,obj,raw))

print("files touched:",{k:len(v) for k,v in sorted(byfile.items())})
report=[]
for fn,edits in sorted(byfile.items()):
    p=os.path.join(ORIG,fn)
    orig=open(p,encoding='utf-8').read()
    txt=orig
    before_md5=hashlib.md5(orig.encode()).hexdigest(); before_len=len(orig.encode())
    expected_delta=0
    for r,obj,raw in edits:
        old_tok='"c":'+json.dumps(r['record_city'],ensure_ascii=False)
        new_tok='"c":'+json.dumps(r['new_city'],ensure_ascii=False)
        assert raw.count(old_tok)==1, f"city token not unique in record {r['name']}"
        new_raw=raw.replace(old_tok,new_tok)
        assert txt.count(raw)==1, f"record raw text not unique in {fn}: {r['name']} count={txt.count(raw)}"
        txt=txt.replace(raw,new_raw,1)
        expected_delta += len(new_raw.encode())-len(raw.encode())
        report.append((fn,r['name'],r['region'],r['record_city'],r['new_city']))
    after=txt.encode()
    assert len(after)-before_len==expected_delta, f"{fn} delta {len(after)-before_len} != {expected_delta}"
    open(os.path.join(BUILT,fn),'w',encoding='utf-8').write(txt)
    # verify parse integrity
    o_recs=[o for o,_ in recs_with_raw(orig)]; n_recs=[o for o,_ in recs_with_raw(txt)]
    assert len(o_recs)==len(n_recs), "record count changed"
    diffs=0
    for a,b in zip(o_recs,n_recs):
        assert sorted(a.keys())==sorted(b.keys()), "field set changed"
        for k in a:
            if a[k]!=b[k]:
                assert k=='c', f"non-city field changed: {k}"
                diffs+=1
    assert diffs==len(edits), f"{fn}: {diffs} changed fields vs {len(edits)} edits"
    print(f"{fn:28} {before_len:>7} -> {len(after):<7} delta={expected_delta:+d}  edits={len(edits)}  md5 {before_md5[:12]} -> {hashlib.md5(after).hexdigest()[:12]}")
    d=list(difflib.unified_diff(orig.splitlines(True),txt.splitlines(True),fromfile="a/"+fn,tofile="b/"+fn,n=0))
    open(os.path.join(DIFFS,fn+".diff"),'w',encoding='utf-8').writelines(d)
json.dump(report,open(os.path.join(BASE,"city-edits.json"),'w'),indent=1)
print("\ntotal edits:",len(report))
