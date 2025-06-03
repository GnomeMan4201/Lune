#!/bin/bash

set -e

echo "[+] Writing clean README.md..."
cat <<EOF > README.md
# Lune DevToolkit XYZ

A modular post-exploitation toolkit for red team operators and adversary simulation.

## Features
- Modular design for flexible payloads and operations
- Includes deception, obfuscation, and tagging components
- Easily extensible

## Installation

TestPyPI:
    pip install --index-url https://test.pypi.org/simple/ lune-devtoolkit-xyz

## Usage

    python -m lune

## Development

    python3 -m venv venv
    source venv/bin/activate
    pip install -e .

## License
MIT
EOF

echo "[+] Creating .gitignore..."
cat <<EOF > .gitignore
*.pyc
__pycache__/
*.egg-info/
dist/
build/
*.log
.env
*.swp
EOF

echo "[+] Adding MIT LICENSE..."
cat <<EOF > LICENSE
MIT License

Copyright (c) $(date +%Y) Nmapkin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...

[truncated for brevity — use full MIT license text in production]
EOF

echo "[+] Creating GitHub Actions workflow for TestPyPI..."
mkdir -p .github/workflows
cat <<EOF > .github/workflows/testpypi-publish.yml
name: Publish to TestPyPI

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade build twine

      - name: Build package
        run: python -m build

      - name: Publish to TestPyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: \${{ secrets.TESTPYPI_API_TOKEN }}
        run: |
          twine upload --repository-url https://test.pypi.org/legacy/ dist/*
EOF

echo "[+] Finalizing git..."
git add .
git commit -m "Finalize repo: clean README, license, .gitignore, CI pipeline"
git tag v0.1.1
git push origin main --tags

echo "[+] Done. Repo is clean, tagged, and CI-ready."
