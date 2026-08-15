#!/usr/bin/env python3
"""
Batch-7 collision gate — EIGHT conditions, seeded.

Run:  python3 gate_b7.py            (real change set)
      python3 gate_b7.py --seed     (inject known-bad rows; every condition must fire)

Conditions
  C1  no new name equals any existing corpus name (corpus-wide, name-only)
  C2  no new name equals another new name
  C3  no new name equals a name in either overrides file
  C4  every suppressed name appears exactly once IN ITS OWN REGION
  C5  no name anywhere contains '|' or '~'
  C6  no name is both SUPPRESSED and ADDED in the same region
  C7  Newfoundland / Nebraska entanglement   (a, b, c)
  C8  city-spelling fold check
"""
import csv, glob, json, re, sys, unicodedata
from collections import Counter, defaultdict

import os
ROOT = os.path.dirname(os.path.abspath(__file__))
SEED = '--seed' in sys.argv

# NOTE: 'Flat Bay' is added in batch 7. The hardcoded nl_cities list in
# sections/tjjm-state-directory.liquid MUST be extended to match, or Golden Rule
# Jiu Jitsu renders on the Nebraska page. Gate and section must stay in lockstep.
NL_CITIES = ["St. John's", "Corner Brook", "Gander", "Paradise",
             "Conception Bay South", "Labrador City", "Grand Falls-Windsor",
             "Clarenville", "Mount Pearl", "Torbay", "Flat Bay"]
NL_SET = set(NL_CITIES)
B7 = ['TN', 'NS', 'NB', 'NL', 'PE', 'DE', 'DC', 'AK']


def region_of(s, c):
    if s == 'NE':
        return 'NL' if c in NL_SET else 'NE'
    return s


def fold(x):
    """City fold: strip accents, lowercase, normalise hyphens/whitespace/punctuation."""
    x = unicodedata.normalize('NFKD', x or '')
    x = ''.join(ch for ch in x if not unicodedata.combining(ch))
    x = x.lower().replace('‐', '-').replace('‑', '-').replace('–', '-').replace('—', '-')
    x = re.sub(r'[\s\-]+', ' ', x)
    x = re.sub(r'[^a-z0-9 ]', '', x)
    return x.strip()


# ---------------------------------------------------------------- load corpus
corpus = json.load(open(f'{ROOT}/scratch/jj-corpus.json', encoding='utf-8'))
corpus_names = set()
corpus_by_region = defaultdict(set)
cities_by_region = defaultdict(set)
for n, c, s, src in corpus:
    corpus_names.add(n)
    code = region_of(s, c)
    corpus_by_region[code].add(n)
    cities_by_region[code].add(c)

# ------------------------------------------------------- load override names
override_names = set()
for fn in ('build-b6b/tjjm-gym-websites-2.liquid',):
    txt = open(f'{ROOT}/{fn}', encoding='utf-8').read()
    override_names |= set(m.group(1).strip() for m in re.finditer(r'~([^|~]+)\|', txt))
# tjjm-gym-websites (file 1) is only on the theme; pull from scratch copy
try:
    txt = open(f'{ROOT}/scratch/live-gym-websites.liquid', encoding='utf-8').read()
    override_names |= set(m.group(1).strip() for m in re.finditer(r'~([^|~]+)\|', txt))
except FileNotFoundError:
    pass
# blank overrides specifically
blank_overrides = set()
for fn in ('build-b6b/tjjm-gym-websites-2.liquid', 'scratch/live-gym-websites.liquid'):
    try:
        txt = open(f'{ROOT}/{fn}', encoding='utf-8').read()
    except FileNotFoundError:
        continue
    for m in re.finditer(r'~([^|~]+)\|([^~]*)~', txt):
        if not m.group(2).strip():
            blank_overrides.add(m.group(1).strip())

# ------------------------------------------------- load existing suppressions
sup_existing = {}
txt = open(f'{ROOT}/build-b6b/tjjm-removed-index.liquid', encoding='utf-8').read()
body = re.sub(r'\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}', '', txt, flags=re.S)
for line in body.split('\n'):
    line = line.strip()
    if not line or '|' not in line:
        continue
    p = line.split('|')
    sup_existing[p[0].strip()] = [x.strip() for x in p[1:] if x.strip()]

# ------------------------------------------------------- load the change set
rows = []
for f in sorted(glob.glob(f'{ROOT}/batches/verdict-b7-*.tsv')):
    rd = list(csv.reader(open(f, encoding='utf-8'), delimiter='\t'))
    h = [x.strip().lower() for x in rd[0]]
    for r in rd[1:]:
        if r and r[0].strip():
            rows.append(dict(zip(h, [c.strip() for c in r])))

adds = []        # (region, name, city, url)
sups = []        # (region, name)
for r in rows:
    act, reg, nm, city = r.get('action'), r.get('region'), r.get('name'), r.get('city')
    if act == 'ADD':
        adds.append((reg, nm, city, r.get('url', '')))
    elif act == 'SUPPRESS':
        sups.append((reg, nm))
    elif act == 'FIX-CITY':
        # rename+recity: legacy blob is unwritable for n/c/s, so suppress+add
        pass

# ---- gate-driven corrections (batches/corrections-b7.tsv) -------------------
corr = []
with open(f'{ROOT}/batches/corrections-b7.tsv', encoding='utf-8') as fh:
    lines = [l for l in fh if not l.startswith('>')]
rd = list(csv.reader(lines, delimiter='\t'))
ch = [x.strip().lower() for x in rd[0]]
for r in rd[1:]:
    if r and r[0].strip():
        corr.append(dict(zip(ch, [c.strip() for c in r])))

fixurl_extra = []
for c in corr:
    if c['op'] == 'RENAME-ADD':
        for i, (reg, nm, city, url) in enumerate(adds):
            if reg == c['region'] and nm == c['old_name'] and city == c['city']:
                adds[i] = (reg, c['new_name'], city, url)
                break
    elif c['op'] == 'ADD-TO-FIXURL':
        adds = [a for a in adds
                if not (a[0] == c['region'] and a[1] == c['old_name'])]
        fixurl_extra.append((c['region'], c['old_name']))
    elif c['op'] == 'DROP-ADD':
        adds = [a for a in adds
                if not (a[0] == c['region'] and a[1] == c['old_name'])]
    elif c['op'] == 'EXTRA-SUPPRESS':
        sups.append((c['region'], c['old_name']))
    elif c['op'] == 'PROMOTE-ADD':
        for r in rows:
            if (r.get('region') == c['region'] and r.get('name') == c['old_name']
                    and r.get('action') == 'NONE'):
                adds.append((c['region'], c['new_name'], c['city'], r.get('url', '')))
                break

# the two DE renames, handled explicitly as suppress+add
RENAMES = [
    ('DE', 'Rehoboth Beach BJJ', 'Rip Tide Brazilian Jiu Jitsu', 'Lewes', 'brazilianjiujitsudelaware.com'),
    ('DE', 'First State BJJ', 'First State Martial Arts Academy', 'Dover', ''),
]
for reg, old, new, city, url in RENAMES:
    sups.append((reg, old))
    adds.append((reg, new, city, url))

if SEED:
    print('!! SEEDED RUN — every condition must fire\n')
    any_corpus = next(iter(corpus_by_region['AK']))
    adds.append(('AK', any_corpus, 'Anchorage', 'x.com'))                    # C1
    adds.append(('TN', 'Seed Dup Name', 'Nashville', 'x.com'))               # C2
    adds.append(('TN', 'Seed Dup Name', 'Memphis', 'x.com'))                 # C2
    if override_names:
        adds.append(('TN', sorted(override_names)[0], 'Nashville', 'x.com'))  # C3
    sups.append(('TN', 'This Name Is Not In Tennessee At All'))              # C4
    adds.append(('TN', 'Seed | Pipe ~ Tilde', 'Nashville', 'x.com'))         # C5
    if sups:
        r0, n0 = sups[0]
        adds.append((r0, n0, 'Seedville', 'x.com'))                          # C6
    adds.append(('NE', 'Seed Nebraska School', "St. John's", 'x.com'))       # C7a
    sups.append(('NE', 'Seed NL Name Collision'))                            # C7b
    adds.append(('NL', 'Seed NL Name Collision', "St. John's", 'x.com'))     # C7b
    # C7c must use a city that is NOT in the permitted list as it currently stands
    adds.append(('NL', 'Seed Unpermitted City', 'Happy Valley-Goose Bay', 'x.com'))
    tn_city = sorted(cities_by_region['TN'])[0]
    adds.append(('TN', 'Seed Fold Case', tn_city.upper() + ' ', 'x.com'))    # C8

# ---------------------------------------------------------------- run gate
fail = Counter()
def bad(cond, msg):
    fail[cond] += 1
    print(f'  [{cond}] {msg}')

print(f'change set: {len(adds)} adds, {len(sups)} suppressions\n')

print('C1  new name vs existing corpus name (corpus-wide)')
for reg, nm, city, url in adds:
    if nm in corpus_names:
        where = [c for c in corpus_by_region if nm in corpus_by_region[c]]
        bad('C1', f'{reg} ADD "{nm}" already exists in corpus (region {where})')
print(f'    -> {fail["C1"]} violations\n')

print('C2  new name vs another new name')
cnt = Counter(nm for _, nm, _, _ in adds)
for nm, k in cnt.items():
    if k > 1:
        regs = [f'{r}/{c}' for r, n, c, _ in adds if n == nm]
        bad('C2', f'"{nm}" proposed {k}x -> {regs}')
print(f'    -> {fail["C2"]} violations\n')

print('C3  new name vs overrides files')
for reg, nm, city, url in adds:
    if nm in override_names:
        tag = ' (BLANK override — would render with no link)' if nm in blank_overrides else ''
        bad('C3', f'{reg} ADD "{nm}" collides with an overrides entry{tag}')
print(f'    -> {fail["C3"]} violations\n')

print('C4  every suppressed name appears exactly once in its own region')
for reg, nm in sups:
    scan = 'NE' if reg == 'NL' else reg
    pool = corpus_by_region.get(reg, set())
    if nm not in pool:
        bad('C4', f'{reg} SUPPRESS "{nm}" is not a record in {reg}')
    else:
        n = sum(1 for x, c, s, _ in corpus if x == nm and region_of(s, c) == reg)
        if n != 1:
            bad('C4', f'{reg} SUPPRESS "{nm}" matches {n} records in {reg}')
print(f'    -> {fail["C4"]} violations\n')

print("C5  no name contains '|' or '~'")
for reg, nm, city, url in adds:
    if '|' in nm or '~' in nm:
        bad('C5', f'{reg} ADD "{nm}" contains a field separator')
for reg, nm in sups:
    if '|' in nm or '~' in nm:
        bad('C5', f'{reg} SUPPRESS "{nm}" contains a field separator')
print(f'    -> {fail["C5"]} violations\n')

print('C6  no name both SUPPRESSED and ADDED in the same region')
supset = set(sups)
renamed = {(r, o) for r, o, _, _, _ in RENAMES}
for reg, nm, city, url in adds:
    if (reg, nm) in supset:
        bad('C6', f'{reg} "{nm}" is both suppressed and added — renders nothing')
print(f'    -> {fail["C6"]} violations\n')

print('C7  Newfoundland / Nebraska entanglement')
ne_sup_all = set(sup_existing.get('NE', [])) | {n for r, n in sups if r in ('NE', 'NL')}
for reg, nm, city, url in adds:
    if reg == 'NE' and city in NL_SET:
        bad('C7a', f'NE ADD "{nm}" uses NL city "{city}" — would render on the NL page')
    if reg == 'NL' and city not in NL_SET:
        bad('C7c', f'NL ADD "{nm}" city "{city}" is outside the permitted list — renders on NEBRASKA')
for reg, nm, city, url in adds:
    if reg == 'NL' and nm in ne_sup_all:
        bad('C7b', f'NL ADD "{nm}" collides with a Nebraska suppression — suppressed on both pages')
for reg, nm in sups:
    if reg == 'NE':
        for r2, n2, c2, _ in adds:
            if r2 == 'NL' and n2 == n2 and n2 == nm:
                bad('C7b', f'NE suppression "{nm}" also suppresses an NL record')
# Nebraska control
ne_live_before = len([1 for n, c, s, _ in corpus
                      if region_of(s, c) == 'NE' and n not in set(sup_existing.get('NE', []))])
ne_delta = len([1 for r, n, c, u in adds if r == 'NE']) - len([1 for r, n in sups if r == 'NE'])
print(f'    Nebraska control: {ne_live_before} live before, delta {ne_delta:+d}')
if ne_delta != 0:
    bad('C7', f'Nebraska count would change by {ne_delta:+d} — batch 7 must not touch Nebraska')
print(f'    -> {fail["C7a"]+fail["C7b"]+fail["C7c"]+fail["C7"]} violations\n')

print('C8  city-spelling fold check')
for reg, nm, city, url in adds:
    f_new = fold(city)
    for existing in cities_by_region.get(reg, set()):
        if existing != city and fold(existing) == f_new:
            bad('C8', f'{reg} ADD city "{city}" folds to existing city "{existing}" — duplicate heading')
newc = defaultdict(dict)
for reg, nm, city, url in adds:
    f_new = fold(city)
    if f_new in newc[reg] and newc[reg][f_new] != city:
        bad('C8', f'{reg} new cities "{city}" and "{newc[reg][f_new]}" fold together')
    newc[reg][f_new] = city
print(f'    -> {fail["C8"]} violations\n')

if '--dump' in sys.argv and not SEED:
    json.dump({'adds': adds, 'sups': sups, 'fixurl_extra': fixurl_extra,
               'renames': RENAMES, 'nl_cities': NL_CITIES},
              open(f'{ROOT}/batches/changeset-b7.json', 'w'), indent=1)
    print('-> wrote batches/changeset-b7.json')

total = sum(fail.values())
print('=' * 60)
if SEED:
    # every sub-condition must be proven independently — grouping C7a/b/c masks failures
    need = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7a', 'C7b', 'C7c', 'C8']
    missing = [c for c in need if fail[c] == 0]
    print('SEEDED RUN: conditions that FIRED:',
          {k: v for k, v in sorted(fail.items()) if v})
    print('SEEDED RUN: conditions that did NOT fire:', missing or 'none — all fired')
    print('RESULT:', 'GATE IS LIVE' if not missing else 'GATE IS BROKEN — fix before trusting a clean run')
else:
    print(f'REAL RUN: {total} violations')
    print('RESULT:', 'CLEAN' if total == 0 else 'BLOCKED')
