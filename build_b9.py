#!/usr/bin/env python3
"""
build_b9.py - batch 9: URL repointing pass (overrides only, no corpus change).

Reads batches/url-overrides-b9.tsv and rewrites:
  snippets/tjjm-gym-websites-2.liquid   (17 in-place edits + 3 stale-line removals)
  snippets/tjjm-gym-websites-3.liquid   (14 appended new entries)

No data file changes. No removed-index changes. Record counts MUST NOT move.

Gates enforced here:
  C3  no name appears in more than one override file, and none twice in one file
  C5  no name contains | or ~
  C9  new_w != stored_w   AND   new_w != current override value
  C11 (new) every target name matches exactly one PUBLISHED record
  BYTES  predicted size of each file asserted under the ~24576 B Admin API ceiling
"""
import csv, json, re, os, sys, collections, hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))
CEIL = 24576
COMMENT = re.compile(r'\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}', re.S)

SRC = {
    'websites-1': 'scratch/live-gym-websites.liquid',
    'websites-2': 'build-b7/tjjm-gym-websites-2.liquid',
    'websites-3': 'build-b7/tjjm-gym-websites-3.liquid',
}
# stale duplicate blank entries superseded by a real URL in websites-3.
# They currently work ONLY because file 3 renders after file 2. Remove them.
STALE_W2_BLANKS = ['Stratford BJJ PEI', 'Team Fortitude NS']
# same name listed twice in websites-2, both blank - drop the second occurrence
DEDUPE_W2 = ['Fighting Gravity Jiu Jitsu']


def p(path):
    return os.path.join(ROOT, path)


def parse(path):
    """-> (list of (name,value) in order, raw text)"""
    txt = open(p(path), encoding='utf-8').read()
    out = []
    for line in COMMENT.sub('', txt).splitlines():
        line = line.strip()
        if not line.startswith('~'):
            continue
        m = re.match(r'~([^|~]+)\|([^~]*)~?$', line)
        if m:
            out.append((m.group(1), m.group(2)))
    return out, txt


def main():
    rows = list(csv.DictReader(open(p('batches/url-overrides-b9.tsv'), encoding='utf-8'), delimiter='\t'))
    corpus = json.load(open(p('scratch/raw-corpus-LL.json'), encoding='utf-8'))
    pubnames = collections.Counter(r['n'] for r in corpus if not r['suppressed'])
    stored = {r['n']: (r['w'] or '') for r in corpus if not r['suppressed']}

    fail = []

    # ---- C5 / C11 ----
    for r in rows:
        n = r['name']
        if '|' in n or '~' in n:
            fail.append(f"C5  {n!r} contains a field separator")
        if pubnames[n] != 1:
            fail.append(f"C11 {n!r} matches {pubnames[n]} published records, expected exactly 1")
        if r['new_w'] == stored.get(n, ''):
            fail.append(f"C9  {n!r} new_w restates the stored value")
        if r['current_override'] and r['new_w'] == r['current_override']:
            fail.append(f"C9b {n!r} new_w restates the current override")
        if not r['new_w'].startswith(('http://', 'https://')):
            fail.append(f"URL {n!r} new_w has no scheme: {r['new_w']!r}")

    dupes = [n for n, c in collections.Counter(r['name'] for r in rows).items() if c > 1]
    for n in dupes:
        fail.append(f"C3  {n!r} appears twice in the override set")

    files = {k: parse(v)[0] for k, v in SRC.items()}
    by_name = {}
    for k, entries in files.items():
        for n, _ in entries:
            by_name.setdefault(n, []).append(k)

    edits = [r for r in rows if r['override_file'] != 'NEW']
    news = [r for r in rows if r['override_file'] == 'NEW']
    for r in edits:
        where = by_name.get(r['name'], [])
        if where != [r['override_file']]:
            fail.append(f"C3  {r['name']!r} expected only in {r['override_file']}, found in {where}")
    for r in news:
        if r['name'] in by_name:
            fail.append(f"C3  {r['name']!r} marked NEW but already present in {by_name[r['name']]}")

    if fail:
        print("GATE FAILED:")
        for f in fail:
            print("  " + f)
        sys.exit(1)
    print(f"GATE PASSED  ({len(rows)} overrides: {len(edits)} edits, {len(news)} new)")

    # ---- rewrite websites-2 ----
    newmap = {r['name']: r['new_w'] for r in edits}
    txt2 = open(p(SRC['websites-2']), encoding='utf-8').read()
    out, seen, removed, applied = [], set(), 0, 0
    for line in txt2.splitlines(keepends=True):
        s = line.strip()
        m = re.match(r'~([^|~]+)\|([^~]*)~?$', s) if s.startswith('~') else None
        if not m:
            out.append(line)
            continue
        n = m.group(1)
        if n in STALE_W2_BLANKS:
            removed += 1
            continue
        if n in DEDUPE_W2 and n in seen:
            removed += 1
            continue
        seen.add(n)
        if n in newmap:
            out.append(f"~{n}|{newmap[n]}~\n")
            applied += 1
        else:
            out.append(line)
    body2 = ''.join(out)
    assert applied == len(edits), f"applied {applied} edits, expected {len(edits)}"
    print(f"websites-2: {applied} edits applied, {removed} stale/duplicate lines removed")

    # ---- append to websites-3 ----
    txt3 = open(p(SRC['websites-3']), encoding='utf-8').read()
    if not txt3.endswith('\n'):
        txt3 += '\n'
    body3 = txt3 + ''.join(f"~{r['name']}|{r['new_w']}~\n" for r in news)
    print(f"websites-3: {len(news)} new entries appended")

    os.makedirs(p('build-b9'), exist_ok=True)
    for name, body, src in [('tjjm-gym-websites-2.liquid', body2, SRC['websites-2']),
                            ('tjjm-gym-websites-3.liquid', body3, SRC['websites-3'])]:
        n = len(body.encode('utf-8'))
        was = os.path.getsize(p(src))
        flag = 'OK' if n < CEIL else 'OVER CEILING'
        print(f"  {name:32} {was:6} -> {n:6} B  ({n-was:+5})  {flag}  md5={hashlib.md5(body.encode('utf-8')).hexdigest()}")
        assert n < CEIL, f"{name} exceeds {CEIL} B"
        open(p('build-b9/' + name), 'w', encoding='utf-8', newline='').write(body)

    # ---- post-condition: parse the built files back ----
    f2 = parse('build-b9/tjjm-gym-websites-2.liquid')[0]
    f3 = parse('build-b9/tjjm-gym-websites-3.liquid')[0]
    f1 = files['websites-1']
    alln = [n for n, _ in f1 + f2 + f3]
    dup = [n for n, c in collections.Counter(alln).items() if c > 1]
    print(f"\npost-build: {len(f1)}+{len(f2)}+{len(f3)} = {len(alln)} override entries")
    print(f"post-build duplicate names across all three files: {dup or 'NONE'}")
    assert not dup
    live = {n: v for n, v in f1 + f2 + f3}
    miss = [r['name'] for r in rows if live.get(r['name']) != r['new_w']]
    print(f"post-build: every new URL present and correct: {'YES' if not miss else miss}")
    assert not miss
    blanks = sum(1 for _, v in f1 + f2 + f3 if v == '')
    print(f"post-build blank (link-killing) entries: {blanks}")


if __name__ == '__main__':
    main()
