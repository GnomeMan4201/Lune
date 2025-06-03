import os
import subprocess
import random
import time
from datetime import datetime

FAKE_FILES = [
    "wallet_seed.png",
    "api_keys_leaked.json",
    "cmd_exec_history.txt",
    "server_backup_03.bak",
    "malware_toolkit_v5.zip"
]

TAG_KEY = "user.schism.fake"
TAG_VALUE = "true"

def tag_file(filepath):
    try:
        subprocess.run(["setfattr", "-n", TAG_KEY, "-v", TAG_VALUE, filepath], check=True)
        print(f"[{datetime.now()}] Tagged {filepath} as fake.")
    except subprocess.CalledProcessError:
        print(f"[!] Failed to tag {filepath}")

def create_fake_files(base_dir="~/lune/deception_artifacts"):
    base_dir = os.path.expanduser(base_dir)
    os.makedirs(base_dir, exist_ok=True)
    for filename in FAKE_FILES:
        full_path = os.path.join(base_dir, filename)
        with open(full_path, "w") as f:
            f.write("This is a decoy file.\n" * random.randint(5, 20))
        tag_file(full_path)
        time.sleep(0.5)

def main():
    print("[+] Covert tagging system initiated.")
    create_fake_files()

if __name__ == '__main__':
    main()
