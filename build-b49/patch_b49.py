#!/usr/bin/env python3
"""batch 49: add a render of tjjm-gym-websites-7 immediately after -6, in both surfaces.
Operates purely on bytes -- the gym-directory header contains multi-byte em dashes, so
character offsets do not equal byte offsets."""
import hashlib, sys, pathlib

B = pathlib.Path("/sessions/youthful-gracious-mccarthy/mnt/TJJM Projects/build-b49")
ANCHOR = b"{%- render 'tjjm-gym-websites-6' -%}"
ADD    = b"{%- render 'tjjm-gym-websites-7' -%}"

ok = True
for name in ("tjjm-state-directory.liquid", "tjjm-gym-directory.liquid"):
    src = (B / "orig" / name).read_bytes()

    n = src.count(ANCHOR)
    if n != 1:
        print(f"FAIL {name}: anchor occurs {n} times, expected 1"); ok = False; continue
    if ADD in src:
        print(f"FAIL {name}: file-7 render already present"); ok = False; continue

    i = src.index(ANCHOR) + len(ANCHOR)      # byte offset of insertion point
    out = src[:i] + ADD + src[i:]

    # byte-level invariants: exactly one insertion of ADD, nothing else touched
    assert len(out) - len(src) == len(ADD),          "length delta wrong"
    assert out[:i] == src[:i],                       "bytes before insertion changed"
    assert out[i:i+len(ADD)] == ADD,                 "inserted bytes wrong"
    assert out[i+len(ADD):] == src[i:],              "bytes after insertion changed"
    assert out.index(ADD) > out.index(ANCHOR),       "file 7 renders before file 6"
    assert out.count(b"\n") == src.count(b"\n"),     "line count changed"
    # every override render still present exactly once
    for k in range(1, 8):
        s = b"'tjjm-gym-websites'" if k == 1 else b"'tjjm-gym-websites-%d'" % k
        assert out.count(s) == 1, f"render {s} not present exactly once"
        if k < 7:
            assert src.count(s) == 1, f"render {s} count changed"

    (B / name).write_bytes(out)
    print(f"OK   {name}: {len(src)} -> {len(out)} bytes (+{len(out)-len(src)})  md5 {hashlib.md5(out).hexdigest()}")

sys.exit(0 if ok else 1)
