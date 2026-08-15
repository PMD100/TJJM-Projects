#!/bin/bash
# STEP 1 of 2 — prepare the repo. This does everything EXCEPT uploading.
# Nothing here touches the internet or your Shopify store. It is safe to re-run.
#
# Run it by pasting this line into Terminal:
#   cd "/Users/Peggie/Downloads/TJJM Projects" && bash push-to-github.sh

set -e
cd "$(dirname "$0")"

echo "==> 1/5  clearing a stuck lock file"
rm -f .git/index.lock

echo "==> 2/5  removing leftover temp files"
find .git/objects -name 'tmp_obj_*' -delete 2>/dev/null || true

echo "==> 3/5  staging everything"
git add -A
echo "         $(git diff --cached --name-only | wc -l | tr -d ' ') files ready"

echo "==> 4/5  saving a snapshot (a 'commit')"
if git rev-parse HEAD >/dev/null 2>&1; then
  echo "         already committed - nothing to do"
else
  git commit -q -m "TJJM gym directory: corpus, build tooling and full audit trail through batch 18

Canonical data and deployment history for thejiujitsumindset.com's BJJ school
directory (5,215 published records / 61 regions).

  scratch/raw-corpus-LL.json   canonical corpus, 5,911 raw stored records
  scratch/raw-datafiles/       all 45 data snippets, MD5-verified vs the live theme
  build-b3..b18/               exact files written to each theme, per batch
  batches/                     verdict TSVs, override manifests, rollback strings
  build_b*.py, gate_b7.py      gate + build scripts
  RULES-tjjm.md                durable rules and their evidence

Rationale: Shopify caps the store at 20 themes, so themes were deleted to stay
under the cap - and the themes were the only record of what had shipped. Four
(HH, II, JJ, KK) are already gone. This repo makes the deployment history
independent of that cap.

Not connected to Shopify. Theme writes go via the Admin API and are MD5-verified."
  echo "         done"
fi

echo "==> 5/5  tidying up and naming the GitHub destination"
git gc -q --prune=now 2>/dev/null || true
git branch -M main
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/PMD100/TJJMgyms.git

echo
echo "-----------------------------------------------------------"
echo " STEP 1 COMPLETE. Nothing has been uploaded yet."
echo
echo " Snapshot saved:"
git log --oneline -1
echo " Files in the snapshot: $(git ls-files | wc -l | tr -d ' ')"
echo " Destination set to:    https://github.com/PMD100/TJJMgyms"
echo
echo " Now do STEP 2 (GitHub Desktop) as described in the chat."
echo "-----------------------------------------------------------"
