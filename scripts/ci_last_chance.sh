#!/bin/bash

echo "[+] Backing up setup..."
cp setup.py setup.py.bak 2>/dev/null

echo "[+] Writing pyproject.toml..."
cat > pyproject.toml <<EOF
[build-system]
requires = ["setuptools>=61", "wheel"]
build-backend = "setuptools.build_meta"
EOF

echo "[+] Cleaning dist..."
rm -rf dist/*
python3 -m build || {
  echo "[!] Build failed — aborting CI run."
  exit 1
}

echo "[+] Committing and tagging for final CI run..."
git add pyproject.toml
git commit -m "🔧 Add pyproject.toml to fix build"
git tag v0.2.1
git push origin main --tags

echo "[✓] Done. CI should now trigger cleanly — walk away, relax."
