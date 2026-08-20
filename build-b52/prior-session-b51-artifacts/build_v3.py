import hashlib, pathlib, sys

SRC = pathlib.Path("../build-b51/built/tjjm-state-directory.v2.liquid")
OUT = pathlib.Path("tjjm-state-directory.v3.liquid")

s = SRC.read_text(encoding="utf-8")
assert hashlib.md5(s.encode()).hexdigest() == "2705ea058de62bb2ce5bffec21ea2cf5", "v2 source drift"

# --- Fix 1: load tjjm-core.js (the file that adds .tjjm-in). Mirrors tjjm-gym-directory.liquid.
old = "{{ 'tjjm-core.css' | asset_url | stylesheet_tag }}\n"
new = "{{ 'tjjm-core.css' | asset_url | stylesheet_tag }}\n<script src=\"{{ 'tjjm-core.js' | asset_url }}\" defer></script>\n"
assert s.count(old) == 1, s.count(old)
s = s.replace(old, new)

# --- Fix 2: no-JS safety net. theme.liquid strips .no-js from <html> as soon as JS runs,
#     so this only applies when scripting is off -> content can never be permanently invisible.
old2 = "section[data-tjjm-statedir].is-filtering .tjjm-reveal{opacity:1;transform:none;transition:none}\n"
new2 = old2 + "html.no-js .tjjm-reveal{opacity:1;transform:none}\n"
assert s.count(old2) == 1
s = s.replace(old2, new2)

# --- Guard: v2 already removed html{scroll-behavior:smooth}; assert it is gone.
assert "scroll-behavior" not in s, "smooth-scroll line must not be present"
assert "tjjm-core.js" in s

b = s.encode("utf-8")
assert len(b) < 24576, len(b)
OUT.write_bytes(b)
print("bytes:", len(b))
print("md5  :", hashlib.md5(b).hexdigest())
