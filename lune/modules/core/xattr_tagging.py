import os
import xattr

FAKE_TAG = b"lune_fake"
REAL_TAG = b"lune_real"

def tag_file(filepath, fake=True):
    tag = FAKE_TAG if fake else REAL_TAG
    try:
        xattr.setxattr(filepath, b"user.lune", tag)
        print(f"[+] Tagged {filepath} as {'fake' if fake else 'real'}")
    except Exception as e:
        print(f"[!] Failed to tag {filepath}: {e}")

def check_tag(filepath):
    try:
        tag = xattr.getxattr(filepath, b"user.lune")
        if tag == FAKE_TAG:
            return "fake"
        elif tag == REAL_TAG:
            return "real"
        else:
            return "unknown"
    except Exception:
        return "untagged"

def scan_directory(path="."):
    print("[*] Scanning for hallucinated files...\n")
    for filename in os.listdir(path):
        status = check_tag(filename)
        if status == "fake":
            print(f"🟥 {filename} [FAKE]")
        elif status == "real":
            print(f"🟩 {filename} [REAL]")
        else:
            print(f"⬜ {filename} [UNMARKED]")

if __name__ == "__main__":
    scan_directory()
