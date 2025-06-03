#!/usr/bin/env python3
import subprocess
import os
import datetime
import webbrowser

def run(cmd, cwd=None):
    print(f"[+] Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True, cwd=cwd)

# 1. Run tests
run("pytest tests")

# 2. Rebuild docs
run("sphinx-build -b html docs/ docs/_build/html")

# 3. Git add + commit if changes
try:
    subprocess.run("git diff --quiet", shell=True, check=True)
    print("[✓] No changes to commit.")
except subprocess.CalledProcessError:
    run('git add .')
    msg = f"Finalize repo at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    run(f'git commit -m "{msg}"')

# 4. Auto tag
today_tag = datetime.datetime.now().strftime("v0.1-%Y%m%d-%H%M")
run(f"git tag {today_tag}")
run("git push")
run("git push --tags")

# 5. Open GitHub Releases page
repo_url = "https://github.com/GnomeMan4201/Lune/releases"
print(f"[✓] Repo finalized and tagged: {today_tag}")
print(f"[🌍] Opening {repo_url}")
webbrowser.open(repo_url)
