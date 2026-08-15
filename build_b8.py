#!/usr/bin/env python3
"""
Duplicate-name disambiguation build. Gates AND builds. Run:
    python3 build_b8.py --seed    # prove every condition fires
    python3 build_b8.py           # gate, then write build-b8/

Base is theme KK (batch 7) == build-b7/. Net corpus change is ZERO: every suppression
is matched by an equal number of re-adds in the same region, so no region count moves
and tjjm-region-index.liquid does not need touching.
"""
import csv, json, os, re, sys, unicodedata
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = f'{ROOT}/build-b7'
OUT = f'{ROOT}/build-b8'
SEED = '--seed' in sys.argv
os.makedirs(OUT, exist_ok=True)

NL_CITIES = set("St. John's|Corner Brook|Gander|Paradise|Conception Bay South|Labrador City|"
                "Grand Falls-Windsor|Clarenville|Mount Pearl|Torbay|Flat Bay".split('|'))
region_of = lambda s, c: ('NL' if c in NL_CITIES else 'NE') if s == 'NE' else s

def fold(x):
    x = unicodedata.normalize('NFKD', x or '')
    x = ''.join(ch for ch in x if not unicodedata.combining(ch)).lower()
    x = re.sub(r'[\s\-]+', ' ', x)
    return re.sub(r'[^a-z0-9 ]', '', x).strip()

# ------------------------------------------------------------------ inputs
corpus = json.load(open(f'{ROOT}/scratch/kk-corpus.json', encoding='utf-8'))
corpus_names = {n for n, c, s, _ in corpus}
by_region = defaultdict(set)
cities_by_region = defaultdict(set)
for n, c, s, _ in corpus:
    by_region[region_of(s, c)].add(n)
    cities_by_region[region_of(s, c)].add(c)

override_names = set()
for fn in ('build-b7/tjjm-gym-websites-2.liquid', 'build-b7/tjjm-gym-websites-3.liquid',
           'scratch/live-gym-websites.liquid', 'build-b6b/tjjm-gym-addresses.liquid'):
    try:
        t = open(f'{ROOT}/{fn}', encoding='utf-8').read()
    except FileNotFoundError:
        continue
    override_names |= {m.group(1).strip() for m in re.finditer(r'~([^|~]+)\|', t)}

lines = [l for l in open(f'{ROOT}/batches/disambiguation-b8.tsv', encoding='utf-8')
         if not l.startswith('>')]
plan = list(csv.DictReader(lines, delimiter='\t'))
for p in plan:
    for k in list(p):
        p[k] = (p[k] or '').strip()

# suppression is by NAME within region; a same-region pair needs ONE entry killing BOTH
sup_names = sorted({(p['s'], p['old_name']) for p in plan})
adds = [(p['s'], p['new_name'], p['city'], p['w'], p['a']) for p in plan]
# names deliberately allowed to match >1 record in their region
MULTI_OK = {(p['s'], p['old_name']) for p in plan if p['kind'] == 'SAME-REGION'}

if SEED:
    print('!! SEEDED RUN — every condition must fire\n')
    adds.append(('AK', sorted(by_region['AK'])[0], 'Anchorage', 'x.com', ''))      # C1
    adds.append(('TX', 'Seed Dup', 'Austin', 'x.com', ''))                          # C2
    adds.append(('TX', 'Seed Dup', 'Dallas', 'x.com', ''))                          # C2
    adds.append(('TX', sorted(override_names)[0], 'Austin', 'x.com', ''))           # C3
    sup_names.append(('TX', 'No Such Record In Texas At All'))                      # C4
    adds.append(('TX', 'Seed | Pipe ~ Tilde', 'Austin', 'x.com', ''))               # C5
    adds.append((plan[0]['s'], plan[0]['old_name'], 'Seedville', 'x.com', ''))      # C6
    adds.append(('TX', 'Seed Fold', sorted(cities_by_region['TX'])[0].upper()+' ', 'x.com', ''))  # C8

# ------------------------------------------------------------------- gate
fail = Counter()
def bad(c, m):
    fail[c] += 1
    print(f'  [{c}] {m}')

print(f'change set: {len(adds)} re-adds, {len(sup_names)} suppression entries\n')

print('C1  new name vs existing corpus name')
for s, n, c, w, a in adds:
    if n in corpus_names:
        bad('C1', f'{s} "{n}" already exists in corpus')
print(f'    -> {fail["C1"]}\n')

print('C2  new name vs another new name')
for n, k in Counter(n for s, n, c, w, a in adds).items():
    if k > 1:
        bad('C2', f'"{n}" proposed {k}x')
print(f'    -> {fail["C2"]}\n')

print('C3  new name vs overrides files')
for s, n, c, w, a in adds:
    if n in override_names:
        bad('C3', f'{s} "{n}" collides with an overrides entry')
print(f'    -> {fail["C3"]}\n')

print('C4  suppressed name matches its own region (multi-match only where declared)')
for s, n in sup_names:
    hits = sum(1 for x, c, st, _ in corpus if x == n and region_of(st, c) == s)
    if hits == 0:
        bad('C4', f'{s} SUPPRESS "{n}" matches no record in {s}')
    elif hits > 1 and (s, n) not in MULTI_OK:
        bad('C4', f'{s} SUPPRESS "{n}" matches {hits} records and is NOT on the multi-match allowlist')
    elif hits > 1:
        print(f'    (declared multi-match: {s} "{n}" kills {hits} records, {hits} re-added)')
print(f'    -> {fail["C4"]}\n')

print("C5  no name contains '|' or '~'")
for s, n, c, w, a in adds:
    if '|' in n or '~' in n or '|' in (a or '') or '~' in (a or ''):
        bad('C5', f'{s} "{n}" or its address contains a field separator')
print(f'    -> {fail["C5"]}\n')

print('C6  no name both suppressed and added in the same region')
sset = set(sup_names)
for s, n, c, w, a in adds:
    if (s, n) in sset:
        bad('C6', f'{s} "{n}" is both suppressed and added')
print(f'    -> {fail["C6"]}\n')

print('C7  Newfoundland / Nebraska')
for s, n, c, w, a in adds:
    if s == 'NE' and c in NL_CITIES:
        bad('C7a', f'NE "{n}" uses NL city "{c}"')
    if s == 'NL' and c not in NL_CITIES:
        bad('C7c', f'NL "{n}" city "{c}" outside permitted list')
touched = {s for s, n, c, w, a in adds} | {s for s, n in sup_names}
print(f'    regions touched: {sorted(touched)}  (NE/NL involved: {bool({"NE","NL"} & touched)})')
print(f'    -> {fail["C7a"]+fail["C7c"]}\n')

print('C8  city-spelling fold check')
for s, n, c, w, a in adds:
    for ex in cities_by_region.get(s, set()):
        if ex != c and fold(ex) == fold(c):
            bad('C8', f'{s} city "{c}" folds to existing "{ex}"')
print(f'    -> {fail["C8"]}\n')

print('C9  per-region net change must be ZERO')
net = Counter()
for s, n, c, w, a in adds:
    net[s] += 1
for s, n in sup_names:
    net[s] -= sum(1 for x, cc, st, _ in corpus if x == n and region_of(st, cc) == s)
for s, v in sorted(net.items()):
    if v != 0:
        bad('C9', f'{s} net change {v:+d} — expected 0')
print(f'    -> {fail["C9"]}\n')

print('C10 no live duplicate names remain after the change')
ri0 = open(f'{SRC}/tjjm-removed-index.liquid', encoding='utf-8').read()
b0 = re.sub(r'\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}', '', ri0, flags=re.S)
sup_now = defaultdict(set)
for l in b0.split('\n'):
    l = l.strip()
    if l and '|' in l:
        p = l.split('|')
        sup_now[p[0].strip()] = {x.strip() for x in p[1:] if x.strip()}
for s, n in sup_names:
    sup_now['NE' if s == 'NL' else s].add(n)
after = [(n, c, region_of(s, c)) for n, c, s, _ in corpus] + \
        [(n, c, s) for s, n, c, w, a in adds]
live = defaultdict(list)
for n, c, r in after:
    if n not in sup_now.get('NE' if r == 'NL' else r, set()):
        live[n].append((c, r))
remaining = {k: v for k, v in live.items() if len(v) > 1}
for k, v in sorted(remaining.items()):
    bad('C10', f'"{k}" still live in {v}')
print(f'    -> {fail["C10"]}\n')

total = sum(fail.values())
print('=' * 62)
if SEED:
    need = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C8']
    missing = [c for c in need if fail[c] == 0]
    print('FIRED:', {k: v for k, v in sorted(fail.items()) if v})
    print('DID NOT FIRE:', missing or 'none — all fired')
    print('RESULT:', 'GATE IS LIVE' if not missing else 'GATE IS BROKEN')
    sys.exit(0)
print(f'REAL RUN: {total} violations —', 'CLEAN' if total == 0 else 'BLOCKED')
if total:
    sys.exit(1)

# ------------------------------------------------------------------ build
recs = []
for s, n, c, w, a in adds:
    r = {'n': n, 'c': c, 's': s}
    if w:
        r['w'] = w
    if a:
        r['a'] = a
    recs.append(r)
recs.sort(key=lambda r: (r['s'], r['c'], r['n']))
esc = lambda v: v.replace('\\', '\\\\').replace('"', '\\"')
out = ['[']
for i, r in enumerate(recs):
    parts = [f'"{k}":"{esc(r[k])}"' for k in ('n', 'c', 's', 'w', 'a') if k in r]
    out.append('{' + ','.join(parts) + '}' + (',' if i < len(recs) - 1 else ''))
out.append(']')
data45 = '\n'.join(out) + '\n'
json.loads(data45)

ri = ri0
for s, n in sorted(sup_names):
    code = 'NE' if s == 'NL' else s
    m = re.search(rf'^{re.escape(code)}\|.*$', ri, re.M)
    if m:
        ri = ri[:m.end()] + '|' + n + ri[m.end():]
    else:
        ri = ri.rstrip('\n') + '\n' + code + '|' + n + '\n'
removed_index = ri

# drop the now-orphaned Infinite Jiu-Jitsu address override
ad = open(f'{ROOT}/build-b6b/tjjm-gym-addresses.liquid', encoding='utf-8').read()
orphan = re.search(r'~Infinite Jiu-Jitsu\|[^~]*~\n?', ad)
assert orphan, 'expected the Infinite Jiu-Jitsu address override'
addresses = ad.replace(orphan.group(0), '')

sec = open(f'{SRC}/tjjm-state-directory.liquid', encoding='utf-8').read()
assert "tjjm-gyms-data-45" not in sec
sec = sec.replace("{%- render 'tjjm-gyms-data-44' -%}{%- endcapture -%}",
                  "{%- render 'tjjm-gyms-data-44' -%}{%- render 'tjjm-gyms-data-45' -%}{%- endcapture -%}")
assert "tjjm-gyms-data-45" in sec
section = sec

files = [('tjjm-gyms-data-45.liquid', data45, None),
         ('tjjm-removed-index.liquid', removed_index, f'{SRC}/tjjm-removed-index.liquid'),
         ('tjjm-gym-addresses.liquid', addresses, f'{ROOT}/build-b6b/tjjm-gym-addresses.liquid'),
         ('tjjm-state-directory.liquid', section, f'{SRC}/tjjm-state-directory.liquid')]
print()
print(f'{"file":<34}{"was":>8}{"predicted":>11}{"delta":>8}{"headroom":>10}')
for name, content, prev in files:
    b = len(content.encode('utf-8'))
    old = len(open(prev, encoding='utf-8').read().encode('utf-8')) if prev else 0
    print(f'{name:<34}{old if prev else "-":>8}{b:>11}{b-old if prev else b:>+8}{24576-b:>10}')
    assert b < 24576, f'{name} exceeds the ceiling'
    open(f'{OUT}/{name}', 'w', encoding='utf-8').write(content)
print(f'\nwrote {len(files)} files to build-b8/   ({len(recs)} re-adds, {len(sup_names)} suppression entries)')
print('region-index NOT changed — every region nets to zero')
