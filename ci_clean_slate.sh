#!/bin/bash
echo "[+] Removing all old workflows..."
rm -f .github/workflows/*.yml

echo "[+] Writing minimal release.yml..."
mkdir -p .github/workflows

cat > .github/workflows/release.yml << 'EOF'
name: Release & Docs

on:
  push:
    tags:
      - 'v*'
  workflow_dispatch:

jobs:
  build-docs:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install Sphinx and theme
        run: |
          python -m pip install --upgrade pip
          pip install sphinx furo

      - name: Patch conf.py
        run: |
          echo "import os, sys; sys.path.insert(0, os.path.abspath('lune'))" >> docs/conf.py

      - name: Build HTML docs
        run: sphinx-build -b html docs docs/_build/html

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: docs/_build/html
EOF

echo "[+] Committing and tagging..."
git add .github/workflows/release.yml
git commit -m "🚀 Clean slate CI: only docs"
git tag v0.3.0
git push origin main --tags

echo "[✓] CI is now docs-only. You’re cleared for launch."
