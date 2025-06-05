#!/bin/bash
set -e

echo "🔧 Bootstrapping your GitHub repo..."

# README.md
cat > README.md <<EOF
# Lune

Lune is a tool designed to [briefly describe its core purpose].

## 🚀 Features
- Feature 1
- Feature 2
- Feature 3

## 🛠️ Installation

\`\`\`bash
git clone https://github.com/GnomeMan4201/Lune.git
cd Lune
# add setup instructions here
\`\`\`

## 📦 Usage

\`\`\`bash
# add usage example
\`\`\`

## 🤝 Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md)

## 📜 License
MIT - see [LICENSE](LICENSE)
EOF

# LICENSE
cat > LICENSE <<EOF
MIT License

Copyright (c) 2025 GnomeMan4201

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
EOF

# CONTRIBUTING.md
cat > CONTRIBUTING.md <<EOF
# Contributing to Lune

Thanks for your interest in contributing!

## How to contribute
1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Push and submit a Pull Request

Please write clear commits and document your code.
EOF

# .gitignore
cat > .gitignore <<EOF
# Python
__pycache__/
*.pyc

# Node
node_modules/
dist/
.env
EOF

# GitHub Actions CI workflow
mkdir -p .github/workflows
cat > .github/workflows/ci.yml <<EOF
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.10
      - name: Install dependencies
        run: |
          pip install -r requirements.txt || echo "No requirements.txt found"
      - name: Run Tests
        run: |
          echo "No test suite defined"
EOF

# EditorConfig
cat > .editorconfig <<EOF
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
indent_style = space
indent_size = 4
trim_trailing_whitespace = true
EOF

echo "✅ Repo is bootstrapped! Review and customize files as needed."
