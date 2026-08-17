#!/usr/bin/env python3
# batch 51 - add city filter + jump-nav to sections/tjjm-state-directory.liquid
# Read from disk, edit in Python, write back. No retyping into a mutation.
import hashlib, os, sys, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(BASE, 'orig',  'tjjm-state-directory.liquid')
DST  = os.path.join(BASE, 'built', 'tjjm-state-directory.liquid')

src = open(SRC, 'rb').read().decode('utf-8')
assert hashlib.md5(src.encode()).hexdigest() == '0aab8efc6be4676b98302596ecdb24ec', 'orig md5 drift'
assert len(src.encode()) == 13339, 'orig size drift'

# ---------------------------------------------------------------- render chain
# Capture the single long override/data render line BEFORE any edit so we can
# prove by byte offset that it survives untouched.
CHAIN_RE = re.compile(r"^\{%- capture gym_json -%\}.*?\{%- endcapture -%\}$", re.M)
m = CHAIN_RE.search(src)
assert m, 'render chain line not found'
chain_line   = m.group(0)
chain_start0 = m.start()
chain_end0   = m.end()
renders0     = re.findall(r"render '([a-z0-9\-]+)'", src)

# ---------------------------------------------------------------- EDIT A
# Fold the city-counting loop into a capture that also collects the city names,
# so the jump-nav can be rendered server-side from `cities`.
A_OLD = """{%- assign gym_count = list.size -%}
{%- assign city_count = 0 -%}
{%- assign prev_city = '' -%}
{%- for item in list limit: 2000 -%}
  {%- assign c0 = item | strip | split: '|' | first -%}
  {%- if c0 != prev_city -%}
    {%- assign city_count = city_count | plus: 1 -%}
    {%- assign prev_city = c0 -%}
  {%- endif -%}
{%- endfor -%}
"""
A_NEW = """{%- assign gym_count = list.size -%}
{%- assign prev_city = '' -%}
{%- capture city_buf -%}
{%- for item in list limit: 2000 -%}
  {%- assign c0 = item | strip | split: '|' | first -%}
  {%- if c0 != prev_city -%}
    {%- assign prev_city = c0 -%}{{ c0 }}~
  {%- endif -%}
{%- endfor -%}
{%- endcapture -%}
{%- assign cities = city_buf | strip | split: '~' -%}
{%- assign city_count = cities.size -%}
"""
assert src.count(A_OLD) == 1, 'EDIT A anchor not unique'
out = src.replace(A_OLD, A_NEW)

# ---------------------------------------------------------------- EDIT B
# Filter UI + server-rendered city jump-nav, at the top of the gym list,
# above the first city heading. Every piece ships in the HTML; `hidden` on the
# filter chrome is removed by JS, so with JS off only the filter chrome is gone.
B_OLD = """    {%- if gym_count > 0 -%}
      {%- assign current_city = '' -%}
"""
B_NEW = """    {%- if gym_count > 0 -%}
      <label class="tjjm-flabel" for="tjjm-q" data-tjjm-tools hidden>Filter by city or gym name</label>
      <div class="tjjm-fbar" data-tjjm-tools hidden>
        <input id="tjjm-q" class="tjjm-finput" type="search" autocomplete="off" spellcheck="false" placeholder="City or gym name">
        <button class="tjjm-fclear" type="button" data-tjjm-clear hidden>Clear</button>
      </div>
      <p class="tjjm-fcount" data-tjjm-tools data-tjjm-count aria-live="polite" aria-atomic="true" hidden>Showing {{ gym_count }} of {{ gym_count }}</p>

      <details class="tjjm-jump"{% if city_count <= 24 %} open{% endif %}>
        <summary class="tjjm-jump-s">Browse by city <em>{{ city_count }}</em></summary>
        <div class="tjjm-jump-b">
          {%- assign prev_l = '' -%}
          {%- for c in cities -%}
            {%- assign cs = c | strip -%}
            {%- if cs == blank -%}{%- continue -%}{%- endif -%}
            {%- assign l = cs | slice: 0 | upcase -%}
            {%- if l != prev_l -%}
              {%- unless prev_l == blank -%}</div>{%- endunless -%}
              {%- assign prev_l = l -%}
              <div class="tjjm-jg"><b class="tjjm-jl" aria-hidden="true">{{ l | escape }}</b>
            {%- endif -%}
            <a class="tjjm-ja" href="#{{ cs | handleize }}">{{ cs | escape }}</a>
          {%- endfor -%}
          {%- unless prev_l == blank -%}</div>{%- endunless -%}
        </div>
      </details>

      <p class="tjjm-p tjjm-nomatch" data-tjjm-none hidden>No schools match that search. <button class="tjjm-fclear" type="button" data-tjjm-clear>Show all {{ gym_count }}</button></p>

      {%- assign current_city = '' -%}
"""
assert out.count(B_OLD) == 1, 'EDIT B anchor not unique'
out = out.replace(B_OLD, B_NEW)

# ---------------------------------------------------------------- EDIT C
# data-c carries the display city so the filter can match on city without
# re-parsing the heading text. Attribute-only change: no structural change.
C_OLD = """<h2 class="tjjm-city-h" id="{{ g_city | handleize }}">"""
C_NEW = """<h2 class="tjjm-city-h" id="{{ g_city | handleize }}" data-c="{{ g_city | escape }}">"""
assert out.count(C_OLD) == 1, 'EDIT C anchor not unique'
out = out.replace(C_OLD, C_NEW)

# ---------------------------------------------------------------- EDIT D
# Inline <style> + <script>, after the existing CSS snippet render so the
# overflow override lands later in the cascade. Colours/fonts/spacing are read
# from assets/tjjm-core.css + snippets/tjjm-statedir-css.liquid; radius stays 0.
CSS_JS = """{%- render 'tjjm-statedir-css' -%}

<style>
section[data-tjjm-statedir]{overflow:clip}
section[data-tjjm-statedir] [hidden]{display:none!important}
.tjjm-flabel{display:block;position:relative;z-index:2;font-size:.75rem;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--dim);margin-bottom:8px}
.tjjm-fbar{position:sticky;top:0;z-index:6;display:flex;gap:8px;background:var(--ink);padding:10px 0;border-bottom:1px solid var(--line)}
.tjjm-finput{flex:1;min-width:0;min-height:44px;padding:10px 14px;background:var(--panel);border:1px solid var(--line);color:var(--bone);font-family:'Inter',sans-serif;font-size:1rem;appearance:none;-webkit-appearance:none}
.tjjm-finput::placeholder{color:var(--dim);opacity:.7}
.tjjm-finput:focus-visible{outline:2px solid var(--red);outline-offset:2px}
.tjjm-fclear{min-height:44px;padding:10px 16px;background:none;border:1px solid var(--line);color:var(--dim);font-family:'Anton',sans-serif;font-size:.85rem;letter-spacing:.12em;text-transform:uppercase;cursor:pointer}
.tjjm-fclear:hover{color:var(--bone);border-color:var(--red)}
.tjjm-fclear:focus-visible{outline:2px solid var(--red);outline-offset:2px}
.tjjm-fcount{position:relative;z-index:2;margin:8px 0 22px;font-size:.85rem;letter-spacing:.06em;color:var(--dim)}
.tjjm-jump{position:relative;z-index:2;border:1px solid var(--line);background:var(--panel);margin:0 0 26px}
.tjjm-jump-s{display:flex;align-items:center;gap:10px;min-height:44px;padding:12px 16px;font-family:'Anton',sans-serif;font-size:.95rem;letter-spacing:.12em;text-transform:uppercase;color:var(--bone);cursor:pointer;list-style:none}
.tjjm-jump-s::-webkit-details-marker{display:none}
.tjjm-jump-s::after{content:"+";margin-left:auto;color:var(--red);font-size:1.25rem;line-height:1}
.tjjm-jump[open] .tjjm-jump-s::after{content:"\\2212"}
.tjjm-jump-s:focus-visible{outline:2px solid var(--red);outline-offset:-2px}
.tjjm-jump-s em{font-style:normal;color:var(--dim);font-size:.85em}
.tjjm-jump-b{padding:2px 16px 12px;border-top:1px solid var(--line)}
.tjjm-jg{display:flex;flex-wrap:wrap;align-items:baseline;gap:0 16px;padding:6px 0;border-bottom:1px solid var(--line)}
.tjjm-jg:last-child{border-bottom:0}
.tjjm-jl{font-family:'Anton',sans-serif;font-weight:400;font-size:.95rem;color:var(--red);flex:none;width:1.5em}
.tjjm-ja{display:inline-block;min-height:40px;padding:7px 0;line-height:26px;font-size:.93rem;color:var(--dim);text-decoration:none}
.tjjm-ja:hover{color:var(--red)}
.tjjm-ja:focus-visible{outline:2px solid var(--red);outline-offset:2px}
.tjjm-ja.is-off{opacity:.3;pointer-events:none}
.tjjm-city-h{scroll-margin-top:84px}
.tjjm-nomatch{margin:26px 0 40px}
section[data-tjjm-statedir].is-filtering .tjjm-reveal{opacity:1;transform:none;transition:none}
@media(prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
@media(max-width:620px){.tjjm-jump-b{padding:2px 12px 10px}.tjjm-jg{gap:0 13px}}
</style>

{%- if gym_count > 0 -%}
<script>
(function(){
var root=document.querySelector('[data-tjjm-statedir]');if(!root)return;
var q=root.querySelector('#tjjm-q');if(!q)return;
var countEl=root.querySelector('[data-tjjm-count]'),noneEl=root.querySelector('[data-tjjm-none]');
function norm(s){s=(s||'').toLowerCase();try{s=s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'')}catch(e){}return s}
var groups=[],byId={},total=0;
[].forEach.call(root.querySelectorAll('h2.tjjm-city-h[id]'),function(h){
  var grid=h.nextElementSibling,city=norm(h.getAttribute('data-c')),items=[];
  if(!grid||grid.className.indexOf('tjjm-gyms')<0)return;
  [].forEach.call(grid.querySelectorAll('.tjjm-gym'),function(el){
    var n=el.querySelector('h3');items.push({el:el,hay:city+' '+norm(n?n.textContent:'')});total++;});
  var g={h:h,grid:grid,items:items};groups.push(g);byId[h.id]=g;});
var jumps=[].slice.call(root.querySelectorAll('.tjjm-ja'));
var clears=[].slice.call(root.querySelectorAll('[data-tjjm-clear]'));
function apply(){
  var v=norm(q.value.trim()),shown=0,i,j,g,it,m,hide;
  root.classList.toggle('is-filtering',!!v);
  for(i=0;i<groups.length;i++){g=groups[i];var vis=0;
    for(j=0;j<g.items.length;j++){it=g.items[j];m=!v||it.hay.indexOf(v)>-1;
      if(it.el.hidden===m)it.el.hidden=!m;if(m)vis++;}
    hide=!!v&&vis===0;
    if(g.h.hidden!==hide){g.h.hidden=hide;g.grid.hidden=hide;}
    shown+=vis;}
  for(i=0;i<jumps.length;i++){g=byId[decodeURIComponent(jumps[i].getAttribute('href').slice(1))];
    if(g)jumps[i].classList.toggle('is-off',!!g.h.hidden);}
  countEl.textContent='Showing '+shown+' of '+total;
  noneEl.hidden=shown>0;
  clears[0].hidden=!v;
}
for(var k=0;k<clears.length;k++)clears[k].addEventListener('click',function(){q.value='';apply();q.focus();});
q.addEventListener('input',apply);
q.addEventListener('keydown',function(e){if(e.key==='Escape'&&q.value){q.value='';apply();}});
[].forEach.call(root.querySelectorAll('[data-tjjm-tools]'),function(e){e.hidden=false});
countEl.textContent='Showing '+total+' of '+total;
})();
</script>
{%- endif -%}
"""
D_OLD = "{%- render 'tjjm-statedir-css' -%}\n"
assert out.count(D_OLD) == 1, 'EDIT D anchor not unique'
out = out.replace(D_OLD, CSS_JS)

# ---------------------------------------------------------------- proofs
data = out.encode('utf-8')
m2 = CHAIN_RE.search(out)
assert m2, 'render chain line lost'
assert m2.group(0) == chain_line, 'render chain line MUTATED'
renders1 = re.findall(r"render '([a-z0-9\-]+)'", out)
assert renders0 == renders1, 'render call list changed'

print('=== render chain byte-offset proof ===')
print('chain line length        : %d bytes (before) / %d bytes (after)' % (
      len(chain_line.encode()), len(m2.group(0).encode())))
print('chain start offset       : %d -> %d  (delta %+d)' % (chain_start0, m2.start(), m2.start()-chain_start0))
print('chain end offset         : %d -> %d  (delta %+d)' % (chain_end0, m2.end(), m2.end()-chain_end0))
print('bytes inserted BEFORE it : %d' % (m2.start()-chain_start0))
print("render '...' calls       : %d -> %d  (identical list: %s)" % (
      len(renders0), len(renders1), renders0 == renders1))
from collections import Counter
c0, c1 = Counter(renders0), Counter(renders1)
print('every render name exactly once: %s' % all(v == 1 for v in c1.values()))
print('names appearing != once       : %s' % [n for n, v in c1.items() if v != 1])
print('raw "render" token count      : %d -> %d' % (src.count('render '), out.count('render ')))

print('\\n=== size / md5 ===')
print('before : %d bytes  %s' % (len(src.encode()), hashlib.md5(src.encode()).hexdigest()))
print('after  : %d bytes  %s' % (len(data), hashlib.md5(data).hexdigest()))
print('delta  : %+d bytes' % (len(data)-len(src.encode())))
assert len(data) < 24576, 'OVER 24576 BYTE CEILING: %d' % len(data)
print('under 24576 ceiling: YES (%d bytes headroom)' % (24576-len(data)))

open(DST, 'wb').write(data)
print('\\nwrote %s' % DST)
