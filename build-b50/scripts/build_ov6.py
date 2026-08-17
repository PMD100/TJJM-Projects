import os,hashlib,difflib,json,re
BASE="/sessions/youthful-gracious-mccarthy/mnt/TJJM Projects/build-b50"
fn="tjjm-gym-websites-6.liquid"
p=os.path.join(BASE,"orig",fn)
orig=open(p,encoding='utf-8').read()
OLD="~Murdoc's Brazilian Jiu-Jitsu (MWBJJ) & Self Defense Academy (GD JJ Affiliate)|~"
NEW="~Murdoc’s Brazilian Jiu-Jitsu (MWBJJ) & Self Defense Academy (GD JJ Affiliate)|~"
assert orig.count(OLD)==1, orig.count(OLD)
assert orig.count(NEW)==0
txt=orig.replace(OLD,NEW,1)
assert txt.count(NEW)==1
b_before=orig.encode(); b_after=txt.encode()
exp=len(NEW.encode())-len(OLD.encode())
assert len(b_after)-len(b_before)==exp, (len(b_after)-len(b_before),exp)
# only that row changed
ol=orig.splitlines(True); nl=txt.splitlines(True)
assert len(ol)==len(nl)
ch=[i for i,(a,b) in enumerate(zip(ol,nl)) if a!=b]
assert len(ch)==1, ch
print("changed line",ch[0]+1)
print("  -",ol[ch[0]].rstrip())
print("  +",nl[ch[0]].rstrip())
open(os.path.join(BASE,"built",fn),'w',encoding='utf-8').write(txt)
open(os.path.join(BASE,"diffs",fn+".diff"),'w',encoding='utf-8').writelines(
    difflib.unified_diff(ol,nl,fromfile="a/"+fn,tofile="b/"+fn,n=1))
print(f"{fn}: {len(b_before)} -> {len(b_after)} bytes (delta {exp:+d})")
print(f"  md5 {hashlib.md5(b_before).hexdigest()} -> {hashlib.md5(b_after).hexdigest()}")
# confirm new name matches a record exactly
corpus=json.load(open('/tmp/corpus.json'))
names=[r for r in corpus if r['n']=="Murdoc’s Brazilian Jiu-Jitsu (MWBJJ) & Self Defense Academy (GD JJ Affiliate)"]
print("record match for curly name:",len(names),names)
