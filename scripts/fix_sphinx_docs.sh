#!/bin/bash
echo '[+] Fixing Sphinx conf.py...'

# Inject sys.path modification right after import section if not already present
PATCH="import os\nimport sys\nsys.path.insert(0, os.path.abspath('..'))"
if ! grep -q "sys\.path\.insert(0, os\.path\.abspath('..'))" docs/conf.py; then
  sed -i "1s;^;${PATCH}\n\n;" docs/conf.py
fi

echo '[+] Committing and tagging...'
git add docs/conf.py
git commit -m "Fix Sphinx module path for CI"
git tag v0.1.7
git push origin main --tags

echo '[✓] Done. Watch Actions tab for green checks.'

