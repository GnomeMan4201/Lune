import os
import readline
from pathlib import Path

# All real files are tagged with this magic string in xattr (or embedded comment, for stealthless fallback)
REAL_TAG = "lune_real"

def list_directory():
    entries = os.listdir()
    for entry in entries:
        try:
            tags = os.getxattr(entry, "user.lune_tag")
            if tags.decode() == REAL_TAG:
                print(f"🟩 {entry}")
            else:
                print(f"🟥 {entry}")
        except (OSError, AttributeError):
            print(f"🟥 {entry}")

def shell():
    while True:
        try:
            cmd = input("💀 traitor > ").strip()
            if cmd == "ls":
                list_directory()
            elif cmd.startswith("cat "):
                _, fname = cmd.split(" ", 1)
                try:
                    tags = os.getxattr(fname, "user.lune_tag")
                    if tags.decode() == REAL_TAG:
                        with open(fname) as f:
                            print(f.read())
                    else:
                        print("🚫 Access denied to hallucinated file.")
                except:
                    print("🚫 File not found or unreadable.")
            elif cmd in ["exit", "quit"]:
                break
            else:
                os.system(cmd)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    shell()
