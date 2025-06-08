# Contributing to Lune

## Setup Instructions

\`\`\`bash
git clone https://github.com/GnomeMan4201/Lune.git
cd Lune
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
\`\`\`

## Guidelines

- Use the main branch for pull requests unless directed otherwise.
- Keep pull requests small and focused (one fix or feature at a time).
- Commit messages should be clear and descriptive (imperative style).
- Update or write tests for any new behavior.
- Do not commit system-specific paths or secrets.
- Ensure code passes linting and tests: \`flake8 . && pytest\`

## Directory Conventions

- \`agents/\`: Agent code and behavior
- \`server/\`: C2 server logic
- \`tests/\`: All test code
- \`data/\`: Task/result JSONs per agent
- \`.github/workflows/\`: CI/CD pipelines and actions

## Submitting

1. Fork the repository
2. Create a feature branch
3. Commit and test your changes
4. Open a pull request to main with a summary of changes
