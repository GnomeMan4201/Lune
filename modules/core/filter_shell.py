import os
import subprocess
from datetime import datetime

TAG_KEY = "user.schism.fake"

def is_fake(filepath):
    try:
        output = subprocess.check_output(["getfattr", "--only-values", "-n", TAG_KEY, filepath], stderr=subprocess.DEVNULL)
        return output.strip() == b"true"
    except subprocess.CalledProcessError:
        return False

def filtered_ls(path="."):
    entries = os.listdir(path)
    for entry in sorted(entries):
        full_path = os.path.join(path, entry)
        if os.path.isfile(full_path):
            tag = "🟥" if is_fake(full_path) else "🟩"
            print(f"{tag} {entry}")
        else:
            print(f"📁 {entry}")

def main():
    print(f"[+] FilterShell started at {datetime.now()}\n")
    cwd = os.getcwd()
    filtered_ls(cwd)

if __name__ == "__main__":
    main()
