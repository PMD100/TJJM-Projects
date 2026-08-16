#!/usr/bin/env python3
# Batch 40 edits. Operates on byte-exact archives pulled from theme 154975109292.
import re, os, hashlib

D = os.path.dirname(os.path.abspath(__file__))
LIMIT = 24576

def read(p):
    with open(os.path.join(D, p), 'r', encoding='utf-8', newline='') as f:
        return f.read()

def write(p, s):
    with open(os.path.join(D, p), 'w', encoding='utf-8', newline='') as f:
        f.write(s)

def strip_comments(s):
    return re.sub(r'\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}', '', s, flags=re.S)

def rows(s):
    """Every ~Name|Value~ outside comment blocks."""
    return re.findall(r'~([^~|]*)\|([^~]*)~', strip_comments(s))

report = []

# ---------- 2a: delete 11 rows from file 3 ----------
F3 = 'tjjm-gym-websites-3.liquid'
DEL = ["Knockout Fitness","GB Clermont","Gracie Barra Blue Ridge","Active Martial Arts",
       "Combat CFMA - Functional Martial Arts","Elementum Jiu-jitsu",
       "Gracie Jiu-Jitsu Altamonte Springs","Gracie Jiu-Jitsu Balance Academy",
       "Hayastan MMA","School of Combat Arts","Wolfpack Brazilian Jiu Jitsu - Martial Arts"]
s3 = read(F3)
lines = s3.split('\n')
deleted, missing, notblank = [], [], []
for name in DEL:
    target = '~' + name + '|~'
    idxs = [i for i, l in enumerate(lines) if l == target]
    if len(idxs) == 1:
        lines[idxs[0]] = None
        deleted.append(name)
    elif len(idxs) == 0:
        # is it present with a URL?
        alt = [l for l in lines if l is not None and l.startswith('~' + name + '|')]
        (notblank if alt else missing).append((name, alt))
    else:
        report.append('2a AMBIGUOUS %r x%d' % (name, len(idxs)))
s3 = '\n'.join([l for l in lines if l is not None])
s3 += ("{%- comment -%}\n"
       "  16 Aug 2026 - BATCH 40. Repo/theme resync. 11 blanking rows deleted from this file:\n"
       "  each carried a blank here AND a live URL in tjjm-gym-websites-6.liquid, so the name\n"
       "  appeared in two override files and broke gate C3. The live rows in -6 are authoritative\n"
       "  and are untouched; only the duplicate blanking row is removed here. Names removed:\n"
       + ''.join("  %s\n" % n for n in DEL) +
       "{%- endcomment -%}\n")
write(F3, s3)
report.append('2a deleted=%d missing=%r not_blank=%r' % (len(deleted), missing, notblank))

# ---------- 2b: 6 blank rows -> live URLs in file 1 ----------
F1 = 'tjjm-gym-websites.liquid'
SET1 = [("Cascade Jiu-Jitsu","https://everettbjj.com/"),
        ("Disciple MMA Academy","https://www.disciplemmaacademy.com/"),
        ("Mid Shore Martial Arts","https://fitnessrxworkout.com/"),
        ("Miller's Martial Arts Academy","https://www.mmaa.com/"),
        ("Odyssey MMA","https://odysseymma.com/"),
        ("Team Reno","http://www.momentumreno.com/")]
s1 = read(F1)
lines = s1.split('\n')
done1, skip1 = [], []
for name, url in SET1:
    target = '~' + name + '|~'
    idxs = [i for i, l in enumerate(lines) if l == target]
    if len(idxs) == 1:
        lines[idxs[0]] = '~' + name + '|' + url + '~'
        done1.append(name)
    else:
        skip1.append((name, len(idxs)))
s1 = '\n'.join(lines)
s1 += ("{%- comment -%}\n"
       "  16 Aug 2026 - BATCH 40. 6 blanking rows above rewritten as live URLs. Each was blanked\n"
       "  in batch 31/32 and has since been re-opened in a browser and re-verified, so the blank\n"
       "  was a false positive. Rewritten in place, not moved, so gate C3 still holds.\n"
       "{%- endcomment -%}\n")
write(F1, s1)
report.append('2b changed=%d skipped=%r' % (len(done1), skip1))

# ---------- 2c: 9 blank rows -> live URLs in file 2 ----------
F2 = 'tjjm-gym-websites-2.liquid'
SET2 = [("GB La Crescenta","https://www.facebook.com/gblacrescenta/"),
        ("Jg Academy Manteca","https://byanymeansjiujitsu.com/"),
        ("Rise Jiu Jitsu Academy","https://www.instagram.com/risejiujitsu/"),
        ("Catch MMA","https://catchmma.com/"),
        ("OC Carlson Gracie Jiu Jitsu","https://www.carlsongracieoc.com/"),
        ("GB Paso Robles","https://graciebarra.com/paso-robles-ca/"),
        ("Ralston Gracie Jiu Jitsu","https://www.facebook.com/ralstongracie"),
        ("Rocknroll Brazilian Jiu Jitsu & Fitness","http://www.rocknrollbjj.com/contact_rocknrollbjj.html"),
        ("Rock And Roll Fight Company","https://rocknrollfightcompany.com/")]
s2 = read(F2)
blank2 = [n for n, v in rows(s2) if v == '']
with open(os.path.join(D, 'file2-blank-rows.txt'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(blank2) + '\n')
report.append('2c file2 total rows=%d blank rows=%d (listed in file2-blank-rows.txt)'
              % (len(rows(s2)), len(blank2)))

lines = s2.split('\n')
done2, skip2 = [], []
for name, url in SET2:
    target = '~' + name + '|~'
    idxs = [i for i, l in enumerate(lines) if l == target]
    if len(idxs) == 1:
        lines[idxs[0]] = '~' + name + '|' + url + '~'
        done2.append((name, url))
    else:
        present_any = [l for l in lines if l.startswith('~' + name + '|')]
        skip2.append((name, 'blank rows found: %d; any row: %d' % (len(idxs), len(present_any))))
s2 = '\n'.join(lines)
s2 += ("{%- comment -%}\n"
       "  16 Aug 2026 - BATCH 40. Blanking rows above rewritten as live URLs from the\n"
       "  link-recovery pass: each URL was opened and its city confirmed. Rewritten in place,\n"
       "  not moved, so gate C3 still holds. Names in the batch-40 list that were NOT already a\n"
       "  blank row in this file were skipped, not invented - they live in another override file\n"
       "  and adding them here would create a duplicate. Applied here:\n"
       + ''.join("  %s\n" % n for n, u in done2) +
       "{%- endcomment -%}\n")
write(F2, s2)
report.append('2c changed=%d skipped=%r' % (len(done2), skip2))

# ---------- sizes ----------
for p in (F1, F2, F3):
    b = open(os.path.join(D, p), 'rb').read()
    report.append('SIZE %-30s %6d bytes  headroom %5d  md5 %s  %s'
                  % (p, len(b), LIMIT - len(b), hashlib.md5(b).hexdigest(),
                     'OK' if len(b) <= LIMIT else '*** OVER LIMIT ***'))

print('\n'.join(report))
