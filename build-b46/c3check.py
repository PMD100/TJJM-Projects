import re,sys,glob,os
names=[l.split('\t')[0] for l in open('worklist.tsv') if l.strip()]
files=sorted(glob.glob('tjjm-gym-websites*.liquid'))
idx={}
for f in files:
    s=open(f,encoding='utf-8').read()
    s=re.sub(r'\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}','',s,flags=re.S)
    for m in re.finditer(r'^~([^|~]*)\|([^~]*)~\s*$',s,flags=re.M):
        idx.setdefault(m.group(1),[]).append(f)
print("files scanned:",files)
print("total rows:",sum(len(v) for v in idx.values()),"distinct names:",len(idx))
dups={k:v for k,v in idx.items() if len(v)>1}
print("DUPLICATE NAMES:",dups if dups else "NONE")
print("--- worklist name presence (exact match) ---")
for n in names:
    print(f"{n!r:55} -> {idx.get(n,'ABSENT')}")
