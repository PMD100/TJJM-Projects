import json, os, glob, re, sys
ORIG="/sessions/youthful-gracious-mccarthy/mnt/TJJM Projects/build-b50/orig"
def files():
    out=[]
    for i in [None]+list(range(2,46)):
        n="tjjm-gyms-data.liquid" if i is None else f"tjjm-gyms-data-{i}.liquid"
        out.append((n, os.path.join(ORIG,n)))
    return out
def parse(path):
    txt=open(path,encoding='utf-8').read()
    recs=[]
    idx=0
    parts=txt.split('{"n":"')
    for chunk in parts[1:]:
        end=chunk.find('}')
        if end<0: raise ValueError("no close brace")
        obj=json.loads('{"n":"'+chunk[:end+1])
        recs.append(obj)
    return txt,recs
if __name__=="__main__":
    total=0; allrecs=[]
    for name,p in files():
        txt,recs=parse(p)
        total+=len(recs)
        for r in recs: allrecs.append((name,r))
    print("TOTAL RECORDS:",total)
    print("FILES:",len(files()))
    json.dump([{"file":f,**r} for f,r in allrecs], open("/tmp/corpus.json","w"))
    # field completeness
    from collections import Counter
    keysets=Counter(tuple(sorted(r.keys())) for _,r in allrecs)
    for k,v in keysets.items(): print("KEYS",k,v)
