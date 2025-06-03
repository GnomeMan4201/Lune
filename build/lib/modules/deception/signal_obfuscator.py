import os
import shutil
import random
from pathlib import Path

REAL_FILE = Path.home() / "real_payload.py"
DECOY_DIR = Path.home() / "Projects/Obfuscated"
FAKE_VARIANTS = 15

def obfuscate():
    if not REAL_FILE.exists():
        print("[!] Real payload not found.")
        return

    DECOY_DIR.mkdir(parents=True, exist_ok=True)

    # Copy real file under disguised name
    real_copy = DECOY_DIR / "notes.py.old.2"
    shutil.copy2(REAL_FILE, real_copy)
    print(f"[+] Copied real payload to: {real_copy}")

    # Create fake/broken variants
    for i in range(FAKE_VARIANTS):
        fake_file = DECOY_DIR / f"notes.py.old.broken_{i}"
        with open(fake_file, "w") as f:
            f.write(f"# Dummy code version {i}\nprint('Broken {i}')\n")
        print(f"[+] Created decoy: {fake_file}")

def main():
    obfuscate()

if __name__ == "__main__":
    main()
