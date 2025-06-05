#!/bin/bash
echo "[+] Writing final CI workflow..."

mkdir -p .github/workflows

cat > .github/workflows/release.yml << 'EOF'
name: Release

on:
  push:
    tags:
      - 'v*'
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install build tools
        run: |
          python -m pip install --upgrade pip build

      - name: Build package
        run: python -m build

  docs:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install docs dependencies
        run: |
          pip install .[docs] || pip install sphinx furo

      - name: Patch conf.py
        run: |
          echo "import os, sys; sys.path.insert(0, os.path.abspath('lune'))" >> docs/conf.py

      - name: Build docs
        run: |
          sphinx-build -b html docs docs/_build/html

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: docs/_build/html
EOF

echo "[+] Committing and tagging..."
git add .github/workflows/release.yml
git commit -m "✅ Final clean CI: build & docs only"
git tag v0.2.3
git push origin main --tags

echo "[✓] Done. CI will build and publish your docs."
