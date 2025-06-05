#!/usr/bin/env python3

import subprocess
import os
from datetime import datetime

def run(cmd, cwd=None):
    print(f"\n[+] Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True, cwd=cwd)

def tag_version():
    tag = datetime.utcnow().strftime("v%Y.%m.%d.%H%M")
    run(f"git tag {tag}")
    run("git push --tags")
    print(f"[✓] Tagged release: {tag}")

def main():
    # Step 1: Ensure dependencies are current
    run("pip install -r requirements.txt")

    # Step 2: Run tests
    run("pytest tests")

    # Step 3: Regenerate docs (auto-imports, new modules)
    run("python3 generate_modules_toc.py")
    run("sphinx-build -b html docs/ docs/_build/html")

    # Step 4: Stage and commit all changes
    run("git add .")
    run('git commit -m "Finalize release: test pass, docs built"')

    # Step 5: Push code and tag version
    run("git push")
    tag_version()

    # Step 6: Open the GitHub Releases page
    repo_url = "https://github.com/GnomeMan4201/Lune/releases"
    run(f"xdg-open {repo_url} || open {repo_url}")

if __name__ == "__main__":
    main()
