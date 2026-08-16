# Batch 40 — repo resynced, invariant restored, 10 more links back.

Session of 16 Aug 2026. Built as theme **SSS** (`154975109292`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**
**Publish SSS `154975109292`.** RRR `154974847148` becomes the rollback.

The large-file work was delegated to an agent that read each file from the theme, edited it with a
script, wrote it back, and checksummed both ends. **That is the fix for the drift problem** — no file
passed through a hand-edit at any point.

---

## The repo is authoritative again

All three out-of-sync files were pulled from the theme and round-tripped byte-exact:

| file | pulled | MD5 confirmed |
|---|---|---|
| `tjjm-gym-websites.liquid` | 23,141 B | `2e92d97a…` ✓ |
| `tjjm-gym-websites-2.liquid` | 21,249 B | `08c1715d…` ✓ |
| `tjjm-gym-websites-3.liquid` | 21,726 B | `00461c4f…` ✓ |

`tjjm-gym-websites-2.liquid` **had never had a local copy in this project.** It does now. All six
override files are archived in `build-b40/`, originals in `build-b40/orig/`.

## Gate C3 is clean

The remaining 11 duplicate rows were deleted from file 3. Then every override file was pulled back
and checked: **1,138 rows, 1,138 distinct names. Zero duplicates.** Confirmed independently on the
live preview.

## Edits applied

| change | result |
|---|---|
| file 3 — delete 11 superseded blanking rows | **11/11** |
| file 1 — restore 6 false positives | **6/6** |
| file 2 — apply 9 pending recoveries | **4/9** |

**Five of the nine were correctly refused**, and this is the gate working exactly as designed:
`GB La Crescenta`, `Jg Academy Manteca`, `Catch MMA` and `Rocknroll Brazilian Jiu Jitsu` live in
file 3, not file 2 — writing them into file 2 would have created a C3 duplicate. And
`OC Carlson Gracie Jiu Jitsu` was **already live at the exact URL** from batch 37, so it needed
nothing. The four remaining still need file 3 edited in place.

### Verified on the SSS preview
```
records published   5,215   unchanged
with a link         4,240   was 4,230 — exactly plus 10
link-free             975
override entries    1,138
duplicate names     NONE
```

| file | final | headroom | MD5 |
|---|---|---|---|
| `tjjm-gym-websites.liquid` | 23,592 B | 984 | `0a102f4828869f4a1d7921f6a4061eaa` |
| `tjjm-gym-websites-2.liquid` | 21,937 B | 2,639 | `580c7d60101558a13bce974dae4adee1` |
| `tjjm-gym-websites-3.liquid` | 22,097 B | 2,479 | `6cdc66976c4ec47cac8ef1be4ed1c703` |

---

## Three restorations that contradicted their own removal notes

The agent flagged, correctly, that three file-1 restorations reverse a **wrong-business** verdict
rather than a dead-link one. Each was re-examined:

- **`Odyssey MMA` → `odysseymma.com`.** Removed as "Odyssey MMA of South Amboy, NJ" — read as a
  different school. The record *is* South Amboy NJ. The original verdict was the error. **Restored.**
- **`Disciple MMA Academy` → `disciplemmaacademy.com`.** Removed as "all locations now
  Greensboro/Burlington NC". The browser re-read shows Northern Virginia, following the Loudoun
  County school calendar. Record region is VA. **Restored.**
- **`Mid Shore Martial Arts` → `fitnessrxworkout.com`.** Removed as "Fitness Rx 24/7 gym, kids
  karate only". I checked this one personally in a browser. The site is Fitness Rx, a 24/7 gym on
  Maryland's Eastern Shore — but its Easton studio page lists **"Disciplines taught: Jiu-Jitsu,
  Karate, Boxing, Taekwondo, Hapkido, Judo, and Wrestling."** Grappling is taught, the city matches
  Easton, and the school appears to have been absorbed into the gym. **Restored — but this is the
  most borderline call in the whole programme.** It is a kids self-defence programme inside a
  fitness gym, not a dedicated academy. Easy to revert if you would rather it showed no link.

All three illustrate the same thing: the original notes were written from **fetched** page bodies,
and the fetcher caches. The browser re-reads are newer and better evidence.

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | **4,240** |
| deliberately link-free | 975 |
| links repointed or restored | **285** |
| of which restored after being wrongly removed | 44 |
| removals re-tested | 343 of 445 |

## Next

1. **Edit file 3 in place** for the four recoveries refused from file 2: `GB La Crescenta`,
   `Jg Academy Manteca`, `Catch MMA`, `Rocknroll Brazilian Jiu Jitsu & Fitness`. File 3 has
   2,479 bytes of headroom.
2. **Finish the removal audit** — about 102 removals still never re-tested.
3. **Reconcile the +1 link delta** noted in batch 39.
4. **The big one: read the 1,994 live links whose pages have never been opened** — 47% of the
   directory, per `AUDIT-COVERAGE-where-we-actually-are.md`.

**Method note for all of the above: delegate large-file edits to an agent that reads, scripts,
writes and checksums.** Batch 40 is the first large-file batch since 36 with zero drift.
