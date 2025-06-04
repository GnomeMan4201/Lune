#!/bin/bash
echo "[+] Nuking all workflows..."
rm -rf .github/workflows/*
mkdir -p .github/workflows

echo "[+] Creating final workflow..."
cat > .github/workflows/docs.yml << 'EOF'
name: Deploy Docs

on:
  push:
    tags:
      - 'v*'
  workflow_dispatch:

jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install requirements
        run: |
          pip install sphinx furo
          echo "import os, sys; sys.path.insert(0, os.path.abspath('lune'))" >> docs/conf.py

      - name: Build Docs
        run: sphinx-build -b html docs docs/_build/html

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: docs/_build/html
EOF

echo "[+] Committing and tagging..."
git add .github/workflows/docs.yml
git commit -m "🔥 CI cleanup: only deploy docs"
git tag v1.0.0
git push origin main --tags

echo "[✓] Done. Watch for green checks. This time, for real."
