import os, sys, hashlib
sys.argv = ['x']
src = open('check_b48.py', encoding='utf-8').read().replace('if __name__ == "__main__":\n    main()', '')
exec(src)

API = {  # checksums re-queried from theme ZZ2 AFTER the write
 "tjjm-gym-websites.liquid":   ("24179", "3abdf7eb0fd5fb7e1e8cd97df2fb4a2d"),
 "tjjm-gym-websites-2.liquid": ("23307", "462b8b03f89f2e9e2450a53b4d5da309"),
 "tjjm-gym-websites-3.liquid": ("23746", "1bd374b1cd8fa1c2236a2dac907d357c"),
 "tjjm-gym-websites-4.liquid": ("22944", "0ef65e0f5f60289380330224a5253b5d"),
 "tjjm-gym-websites-5.liquid": ("2593",  "70fa4a3b8526024fe7e6431c3002b88e"),
 "tjjm-gym-websites-6.liquid": ("19823", "9749cb35614e91953115af00c436a798"),
}
idx, total, distinct, c3ok = gate_c3(BUILD, "POST-WRITE (local build == theme)")

print("\n=== API vs LOCAL checksum reconciliation ===")
allok = True
for f, (sz, md5) in API.items():
    p = os.path.join(BUILD, f)
    lm = hashlib.md5(open(p, 'rb').read()).hexdigest()
    ls = str(os.path.getsize(p))
    ok = (lm == md5 and ls == sz)
    allok &= ok
    print(f"  {f:32s} api={sz:>6}/{md5}  local={ls:>6}/{lm}  {'MATCH' if ok else '*** MISMATCH ***'}")
print("ALL SIX MATCH:", allok)

print("\n=== batch 48 rows present in written files ===")
import csv
rows = list(csv.DictReader(open(os.path.join(BUILD, 'apply-b48.tsv'), encoding='utf-8'), delimiter='\t'))
miss = 0
for r in rows:
    want = r['new_url'].strip() if r['action'] == 'REPOINT' else ''
    got = None
    for f in FILES:
        for n, v in parse(os.path.join(BUILD, f)):
            if n == r['name']:
                got = (f, v)
    if got is None or got[1] != want:
        miss += 1
        print("  *** NOT APPLIED:", r['name'], got)
print(f"all 30 rows applied with correct value: {miss == 0}")
print(f"\nTOTAL rows {total}  DISTINCT {distinct}  equal={total==distinct}  C3_clean={c3ok}")
print(f"file 6 headroom left: {24576 - os.path.getsize(os.path.join(BUILD,'tjjm-gym-websites-6.liquid'))} bytes")
