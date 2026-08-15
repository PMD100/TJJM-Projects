#!/usr/bin/env python3
"""
Batch-7 build. Generates every file into build-b7/ and PREDICTS each byte size
before writing, per the project rule. Nothing here touches a theme.

Files produced:
  snippets/tjjm-gyms-data-44.liquid      NEW  - the 56 new records
  snippets/tjjm-gym-websites-2.liquid    EDIT - one blank override filled in place
  snippets/tjjm-gym-websites-3.liquid    NEW  - batch-7 URL fixes (websites-2 is near its ceiling)
  snippets/tjjm-removed-index.liquid     EDIT - 7 new region rows + 3 names appended to the NE row
  sections/tjjm-state-directory.liquid   EDIT - 2 render tags, nl_cities + Flat Bay, comment total
  snippets/tjjm-region-index.liquid      EDIT - 8 region counts + comment total
"""
import json, os, re, csv, glob, unicodedata

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = f'{ROOT}/build-b6b'
OUT = f'{ROOT}/build-b7'
os.makedirs(OUT, exist_ok=True)

cs = json.load(open(f'{ROOT}/batches/changeset-b7.json'))
adds, sups = cs['adds'], cs['sups']
NL_CITIES = cs['nl_cities']

# ---------------------------------------------------------------- addresses
raw = json.load(open(f'{ROOT}/batches/addr-b7.json'))
CAVEAT = re.compile(r'third-party|per search|not confirmed|not found|unverified|n/a|per directories',
                    re.I)
addr = {}
for key, val in raw.items():
    reg, nm = key.split('|', 1)
    v = val.strip()
    if CAVEAT.search(v):
        continue
    if not re.match(r'^\d', v):          # must start with a street number
        continue
    city = next((c for r, n, c, u in adds if r == reg and n == nm), None)
    if not city:
        continue
    base = city.split('(')[0].split('/')[0].strip()
    if base.lower() not in v.lower():    # address must name the record's own city
        continue
    v = re.sub(r'\s*\(.*?\)\s*$', '', v).strip()
    if '|' in v or '~' in v:
        continue
    addr[(reg, nm)] = v
print(f'addresses accepted after strict filtering: {len(addr)} of {len(raw)}')

# ---------------------------------------------------------- 1. data file 44
def storage_code(reg):
    """Newfoundland is stored under Nebraska's code; the section re-files by city."""
    return 'NE' if reg == 'NL' else reg

recs = []
for reg, nm, city, url in adds:
    city = city.split('(')[0].strip().rstrip(',')
    if ',' in city:                       # "Miramichi, NB" -> "Miramichi"
        city = city.split(',')[0].strip()
    w = (url or '').strip()
    if w in ('(none)', '-', 'n/a', 'None'):
        w = ''
    w = w.split('?')[0].rstrip('/') if w else ''
    recs.append({'n': nm, 'c': city, 's': storage_code(reg), 'w': w,
                 'a': addr.get((reg, nm), '')})

for r in recs:
    for k in ('n', 'c'):
        assert '|' not in r[k] and '~' not in r[k], f'separator in {r[k]!r}'

recs.sort(key=lambda r: (r['s'], r['c'], r['n']))

def esc(v):
    return v.replace('\\', '\\\\').replace('"', '\\"')

lines = ['[']
for i, r in enumerate(recs):
    parts = [f'"n":"{esc(r["n"])}"', f'"c":"{esc(r["c"])}"', f'"s":"{esc(r["s"])}"']
    if r['w']:
        parts.append(f'"w":"{esc(r["w"])}"')
    if r['a']:
        parts.append(f'"a":"{esc(r["a"])}"')
    lines.append('{' + ','.join(parts) + '}' + (',' if i < len(recs) - 1 else ''))
lines.append(']')
data44 = '\n'.join(lines) + '\n'

# --------------------------------------------------- 2. removed-index update
ri = open(f'{SRC}/tjjm-removed-index.liquid', encoding='utf-8').read()
sup_by_region = {}
for reg, nm in sups:
    sup_by_region.setdefault('NE' if reg == 'NL' else reg, []).append(nm)

for code, names in sup_by_region.items():
    names = sorted(set(names))
    row_re = re.compile(rf'^{re.escape(code)}\|.*$', re.M)
    m = row_re.search(ri)
    if m:                                   # existing row (NE) -> append
        ri = ri[:m.end()] + '|' + '|'.join(names) + ri[m.end():]
    else:                                   # new region row -> append at end
        ri = ri.rstrip('\n') + '\n' + code + '|' + '|'.join(names) + '\n'
removed_index = ri

# ------------------------------------------------------ 3. websites-3 (new)
rows = []
for f in sorted(glob.glob(f'{ROOT}/batches/verdict-b7-*.tsv')):
    rd = list(csv.reader(open(f, encoding='utf-8'), delimiter='\t'))
    h = [x.strip().lower() for x in rd[0]]
    for r in rd[1:]:
        if r and r[0].strip():
            rows.append(dict(zip(h, [c.strip() for c in r])))

corpus = json.load(open(f'{ROOT}/scratch/jj-corpus.json', encoding='utf-8'))
stored_names = {n for n, c, s, _ in corpus}

# Overrides come from the audited table, NOT the verdict TSVs' `url` column - that
# column mixes stored and corrected URLs and would have produced four no-op overrides.
ov_lines = [l for l in open(f'{ROOT}/batches/url-overrides-b7.tsv', encoding='utf-8')
            if not l.startswith('>')]
ov = list(csv.DictReader(ov_lines, delimiter='\t'))

fixes, file2_edit = {}, None
for o in ov:
    nm = o['name'].strip()
    new = (o['new_w'] or '').strip()
    old = (o['stored_w'] or '').strip()
    assert nm in stored_names, f'override for unknown record {nm!r}'
    assert new != old, f'override for {nm!r} restates the stored value'
    assert '|' not in nm and '~' not in nm and '|' not in new and '~' not in new
    if o['file'].strip() == '2':
        file2_edit = (nm, new)
    else:
        fixes[nm] = new
print(f'overrides: {len(fixes)} in file 3, {1 if file2_edit else 0} edited in file 2')

w3 = ['{%- comment -%}',
      '  TJJM gym-website overrides, file 3. Created in batch 7 because',
      '  tjjm-gym-websites-2 reached ~20.5 KB against the Admin API\'s ~24 KB',
      '  rewrite ceiling. Same format as files 1 and 2: ~Name|URL~',
      '  An EMPTY value blanks the link. Only add an entry that CHANGES something -',
      '  restating a stored value pins it as a second source of truth.',
      '  Rendered after files 1 and 2 by sections/tjjm-state-directory.liquid.',
      '{%- endcomment -%}']
for nm in sorted(fixes):
    w3.append(f'~{nm}|{fixes[nm]}~')
websites3 = '\n'.join(w3) + '\n'

# --------------------------------------------- 4. websites-2 in-place edit
w2 = open(f'{SRC}/tjjm-gym-websites-2.liquid', encoding='utf-8').read()
assert file2_edit, 'expected exactly one file-2 override edit'
nm2, new2 = file2_edit
OLD = f'~{nm2}|~'
NEW = f'~{nm2}|{new2}~'
assert w2.count(OLD) == 1, f'expected one blank override for {nm2!r}, found {w2.count(OLD)}'
websites2 = w2.replace(OLD, NEW)

# ------------------------------------------------------------- 5. section
sec = open(f'{SRC}/tjjm-state-directory.liquid', encoding='utf-8').read()
assert "{%- render 'tjjm-gyms-data-44' -%}" not in sec
sec = sec.replace("{%- render 'tjjm-gyms-data-43' -%}{%- endcapture -%}",
                  "{%- render 'tjjm-gyms-data-43' -%}{%- render 'tjjm-gyms-data-44' -%}{%- endcapture -%}")
sec = sec.replace("{%- render 'tjjm-gym-websites-2' -%}{%- endcapture -%}",
                  "{%- render 'tjjm-gym-websites-2' -%}{%- render 'tjjm-gym-websites-3' -%}{%- endcapture -%}")
old_nl = "{%- assign nl_cities = \"St. John's|Corner Brook|Gander|Paradise|Conception Bay South|Labrador City|Grand Falls-Windsor|Clarenville|Mount Pearl|Torbay\" | split: '|' -%}"
new_nl = "{%- assign nl_cities = \"St. John's|Corner Brook|Gander|Paradise|Conception Bay South|Labrador City|Grand Falls-Windsor|Clarenville|Mount Pearl|Torbay|Flat Bay\" | split: '|' -%}"
assert old_nl in sec, 'nl_cities line not found verbatim'
sec = sec.replace(old_nl, new_nl)
section = sec

# --------------------------------------------------------- 6. region index
rix = open(f'{SRC}/tjjm-region-index.liquid', encoding='utf-8').read()
rc = lambda s, ci: ('NL' if ci in NL_CITIES else 'NE') if s == 'NE' else s
stored_ct = {}
for n, ci, s, _ in corpus:
    k = rc(s, ci)
    stored_ct[k] = stored_ct.get(k, 0) + 1
from collections import Counter
ac, sc = Counter(r for r, _, _, _ in adds), Counter(r for r, _ in sups)
newcount = {r: stored_ct[r] - sc[r] + ac[r] for r in ['TN','NS','AK','NB','NL','PE','DE','DC']}
for code, cnt in newcount.items():
    m = re.search(rf'^([a-z0-9-]+)\|([^|]+)\|(\d+)\|{code}\|(\w+)$', rix, re.M)
    assert m, f'region index row for {code} not found'
    rix = rix[:m.start()] + f'{m.group(1)}|{m.group(2)}|{cnt}|{code}|{m.group(4)}' + rix[m.end():]
rix = rix.replace('Verified total across all 61 regions: 5,205.',
                  'Verified total across all 61 regions: 5,219.')
region_index = rix

# --------------------------------------------------------------- summary
files = [
    ('tjjm-gyms-data-44.liquid',    data44,        None),
    ('tjjm-gym-websites-2.liquid',  websites2,     f'{SRC}/tjjm-gym-websites-2.liquid'),
    ('tjjm-gym-websites-3.liquid',  websites3,     None),
    ('tjjm-removed-index.liquid',   removed_index, f'{SRC}/tjjm-removed-index.liquid'),
    ('tjjm-state-directory.liquid', section,       f'{SRC}/tjjm-state-directory.liquid'),
    ('tjjm-region-index.liquid',    region_index,  f'{SRC}/tjjm-region-index.liquid'),
]
CEIL = 24576
print()
print(f'{"file":<34}{"was":>8}{"predicted":>11}{"delta":>8}{"headroom":>10}')
for name, content, prev in files:
    b = len(content.encode('utf-8'))
    old = len(open(prev, encoding='utf-8').read().encode('utf-8')) if prev else 0
    print(f'{name:<34}{old if prev else "-":>8}{b:>11}{b-old if prev else b:>+8}{CEIL-b:>10}')
    assert b < CEIL, f'{name} EXCEEDS the ~24 KB ceiling'

for name, content, _ in files:
    with open(f'{OUT}/{name}', 'w', encoding='utf-8') as fh:
        fh.write(content)
print(f'\nwrote {len(files)} files to build-b7/')
print(f'new records: {len(recs)}   suppressions: {len(sups)}   url overrides in file 3: {len(fixes)}')
