import json, os, re, sys, collections
ORIG = 'build-b50b/orig'

def parse_file(path):
    """Files are not uniformly valid JSON (29-34 are bare concatenated objects).
    Split on '{"n":"' and take up to the next '}'."""
    s = open(path, encoding='utf-8').read()
    out = []
    parts = s.split('{"n":"')
    for chunk in parts[1:]:
        end = chunk.find('}')
        if end < 0:
            continue
        try:
            r = json.loads('{"n":"' + chunk[:end+1])
        except Exception:
            continue
        out.append(r)
    return out

files = sorted([f for f in os.listdir(ORIG) if re.fullmatch(r'tjjm-gyms-data(-\d+)?\.liquid', f)],
               key=lambda f: int(re.search(r'-(\d+)\.', f).group(1)) if re.search(r'-(\d+)\.', f) else 0)
assert len(files) == 45, len(files)

recs = []
for f in files:
    for r in parse_file(os.path.join(ORIG, f)):
        r['_file'] = f
        recs.append(r)
print('TOTAL RECORDS PARSED:', len(recs))

# removed index
rem = collections.defaultdict(set)
for line in open(os.path.join(ORIG,'tjjm-removed-index.liquid'), encoding='utf-8').split('\n') if False else open(os.path.join(ORIG,'tjjm-removed-index.liquid'), encoding='utf-8'):
    l = line.strip()
    if not l or '|' not in l or l.startswith('{%'):
        continue
    p = l.split('|')
    code = p[0].strip()
    if not re.fullmatch(r'[A-Z]{2}', code):
        continue
    for n in p[1:]:
        n = n.strip()
        if n:
            rem[code].add(n)

NLC = ["St. John's","Corner Brook","Gander","Paradise","Conception Bay South",
       "Labrador City","Grand Falls-Windsor","Clarenville","Mount Pearl","Torbay","Flat Bay"]

published = []
for r in recs:
    n = (r.get('n') or '').strip()
    s = (r.get('s') or '').strip()
    c = (r.get('c') or '').strip()
    if not n:
        continue
    if n in rem.get(s, ()):
        continue
    code = 'NL' if (s == 'NE' and c in NLC) else s
    published.append((n, c, code, s))
print('PUBLISHED (after removed-index):', len(published))
regions = collections.Counter(code for _,_,code,_ in published)
print('REGIONS:', len(regions))
json.dump({f'{k}': v for k, v in sorted(regions.items())}, open('build-b50b/region-counts-before.json','w'), indent=0)

# name -> record index (over ALL records, published or not)
byname = collections.defaultdict(list)
for r in recs:
    byname[(r.get('n') or '').strip()].append(r)
dupes = {k: v for k, v in byname.items() if len(v) > 1}
print('DUPLICATED NAMES:', len(dupes), ' surplus records:', sum(len(v)-1 for v in dupes.values()))

# ---- gate: exactly one record per override name ----
rows = [l.rstrip('\n').split('\t') for l in open('scratch/identity/apply-b50-city.tsv', encoding='utf-8')]
hdr = rows[0]; data = rows[1:]
ci = {h:i for i,h in enumerate(hdr)}
print('\nTSV rows:', len(data))
ok, bad = [], []
for row in data:
    name = row[ci['name']]; reg = row[ci['region']]
    rc = row[ci['record_city']]; nc = row[ci['new_city']]
    m = byname.get(name, [])
    status = []
    if len(m) != 1:
        status.append(f'MATCHES={len(m)}')
    if '|' in name or '~' in name:
        status.append('C5-FAIL')
    if not nc.strip():
        status.append('EMPTY-VALUE')
    if len(m) == 1:
        r = m[0]
        if (r.get('s') or '').strip() != reg: status.append(f"REGION-MISMATCH(rec={r.get('s')})")
        if (r.get('c') or '').strip() != rc:  status.append(f"CITY-MISMATCH(rec={r.get('c')})")
    tag = 'OK' if not status else ';'.join(status)
    print(f"  {'OK ' if not status else 'XX '} {name:45s} {reg} {rc:26s} -> {nc:20s} file={m[0]['_file'] if len(m)==1 else '-':26s} {tag if status else ''}")
    (ok if not status else bad).append((name, nc, tag))
print(f'\nGATE: {len(ok)} clean, {len(bad)} flagged')
json.dump([[n, c] for n, c, _ in ok] + [[n, c] for n, c, _ in bad], open('build-b50b/city-rows.json','w'), indent=1)
