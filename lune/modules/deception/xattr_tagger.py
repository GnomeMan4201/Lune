import os
import sys
import subprocess

def tag_file(filepath):
    try:
        subprocess.run(["xattr", "-w", "user.fake", "true", filepath], check=True)
        print(f"[+] Tagged {filepath} with xattr user.fake=true")
    except subprocess.CalledProcessError:
        print(f"[!] Failed to tag {filepath}")

def check_tag(filepath):
    try:
        result = subprocess.run(["xattr", "-p", "user.fake", filepath], capture_output=True, text=True)
        if "true" in result.stdout.strip():
            print(f"[!] FAKE FILE: {filepath}")
        else:
            print(f"[+] REAL FILE: {filepath}")
    except subprocess.CalledProcessError:
        print(f"[+] REAL FILE: {filepath}")

def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ["tag", "check"]:
        print("Usage: python3 xattr_tagger.py [tag|check] <filename>")
        return
    cmd, file = sys.argv[1], sys.argv[2]
    if not os.path.exists(file):
        print("[!] File does not exist.")
        return
    if cmd == "tag":
        tag_file(file)
    elif cmd == "check":
        check_tag(file)

if __name__ == "__main__":
    main()
