import os
import random
from pathlib import Path

FAKE_DOCS = [
    "Q3VzdG9tZXIgTG9naW4gRGF0YQpVc2VybmFtZTogam9obmRvZQpQYXNzd29yZDogc2VjdXJlcGFzczEyMw==",  # base64 blob
    "<html><body><h1>Internal Pen Test Notes</h1><p>Do not share</p></body></html>",
    "client_secret = 'FAKE-1234-SECRET-XYZ'",
]

FAKE_LOG_LINES = [
    "Accepted publickey for admin from 192.168.1.101 port 54522",
    "sudo:   evilscript.sh : command not found",
    "Failed password for root from 10.0.2.15 port 44875 ssh2",
]

def drop_decoys():
    decoy_dir = Path.home() / "Documents/Reports"
    decoy_dir.mkdir(parents=True, exist_ok=True)
    for i in range(3):
        fake_file = decoy_dir / f"suspicious_note_{i+1}.txt"
        fake_file.write_text(random.choice(FAKE_DOCS))
    print("[mirrorshade] Dropped fake documents.")

def poison_syslog():
    log_path = "/var/log/syslog"
    if os.access(log_path, os.W_OK):
        with open(log_path, "a") as log:
            for _ in range(3):
                log.write(random.choice(FAKE_LOG_LINES) + "\n")
        print("[mirrorshade] Appended fake syslog entries.")
    else:
        print("[mirrorshade] Insufficient permissions to modify /var/log/syslog.")

def main():
    drop_decoys()
    poison_syslog()

if __name__ == "__main__":
    main()
