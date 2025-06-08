# Project Directory Structure - Lune

This document outlines the structure and purpose of directories and key files within the Lune framework.

Lune/
├── agents/                # Agent logic (beaconing)
│   └── lune_agent.py
├── server/                # Flask C2 server
│   └── c2.py
├── data/                  # JSON per-agent task files
│   └── agent_001_tasks.json
├── tests/                 # Unit and integration tests
│   └── test_c2.py
├── .github/workflows/     # GitHub Actions config
│   └── ci.yml
├── docs/                  # Design docs (optional)
├── requirements.txt       # Python dependencies
├── README.md              # Main overview
├── PROJECT_STRUCTURE.md
├── ARCHITECTURE.md
├── DESIGN_NOTES.md
├── CONTRIBUTING.md
└── LICENSE
