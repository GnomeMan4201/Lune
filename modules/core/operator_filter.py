import os
import subprocess
from pathlib import Path

TARGET_DIR = Path.home() / "Projects/Obfuscated"

def list_files_with_tags():
    print("\n🧠 Operator Filter Lens View\n")
    for file in sorted(TARGET_DIR.glob("*")):
        tag = get_tag(file)
        symbol = {
            "real": "🟩",
            "fake": "🟥",
            "unknown": "⬜"
        }.get(tag, "⬜")

        print(f"{symbol} {file.name}")

def get_tag(file_path):
    try:
        output = subprocess.check_output(["xattr", file_path])
        if b"user.trust" in output:
            tag = subprocess.check_output(["xattr", "-p", "user.trust", file_path])
            return tag.decode().strip()
        return "unknown"
    except subprocess.CalledProcessError:
        return "unknown"

def main():
    if not TARGET_DIR.exists():
        print(f"[!] Target directory {TARGET_DIR} not found.")
        return
    list_files_with_tags()

if __name__ == "__main__":
    main()
