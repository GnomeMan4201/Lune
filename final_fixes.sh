#!/bin/bash
set -e

echo "[+] Bumping version to v0.1.5..."
sed -i 's/version="0.1.4"/version="0.1.5"/g' setup.py

echo "[+] Patching conf.py for Sphinx path..."
echo "import os, sys; sys.path.insert(0, os.path.abspath('lune'))" >> docs/conf.py

echo "[+] Committing changes and tagging..."
git add setup.py docs/conf.py
git commit -m "Fix Sphinx path, bump version to 0.1.5"
git tag v0.1.5
git push origin main --tags

echo "[✓] All fixes applied. CI will run and should now pass."
