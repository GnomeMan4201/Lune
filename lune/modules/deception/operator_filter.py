import os
import subprocess
from pathlib import Path

TAG_DB = "modules/deception/.fake_tags"

def load_fake_tags():
    if not os.path.exists(TAG_DB):
        return set()
    with open(TAG_DB, "r") as f:
        return set(line.strip() for line in f)

def colorize(filename, fake_tags):
    if filename in fake_tags:
        return f"\033[91m🟥 {filename}\033[0m"
    else:
        return f"\033[92m🟩 {filename}\033[0m"

def ls_overlay():
    fake_tags = load_fake_tags()
    files = os.listdir(".")
    for f in sorted(files):
        print(colorize(f, fake_tags))

def tag_fake_file(filename):
    with open(TAG_DB, "a") as f:
        f.write(f"{filename}\n")
    print(f"[+] Tagged {filename} as FAKE.")

def main():
    print("╭──────────────────────────────╮")
    print("│       Operator Filter        │")
    print("╰──────────────────────────────╯")
    print("[1] View directory with tags")
    print("[2] Tag a file as fake")
    print("[3] Exit")
    choice = input("Select: ").strip()
    if choice == "1":
        ls_overlay()
    elif choice == "2":
        filename = input("File to tag: ").strip()
        if os.path.exists(filename):
            tag_fake_file(filename)
        else:
            print("[!] File not found.")
    else:
        print("Bye.")

if __name__ == "__main__":
    main()
