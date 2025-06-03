import os
import json
import random

FAKE_FILES = [
    ("~/.bash_history", "shell"),
    ("~/Downloads/malware_toolkit_v5.zip", "payload"),
    ("~/Documents/fake_contract.docx", "decoy"),
    ("~/wallet_seed.png", "crypto"),
    ("~/projects/exploit_2025.py", "exploit")
]

TAG_DB_PATH = os.path.expanduser("~/.perception_tags.json")

def apply_fake_artifacts():
    print("[*] Injecting fake artifacts...")
    tag_db = {}
    for path, tag in FAKE_FILES:
        full_path = os.path.expanduser(path)
        try:
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, "w") as f:
                f.write(f"# This is a {tag} placeholder.\n{random.randint(1000,9999)}")
            tag_db[full_path] = {"type": tag, "real": False}
        except Exception as e:
            print(f"[!] Failed to create {path}: {e}")

    try:
        with open(TAG_DB_PATH, "w") as tagfile:
            json.dump(tag_db, tagfile)
        print("[+] Tag database saved.")
    except Exception as e:
        print(f"[!] Failed to save tag DB: {e}")

def main():
    print("🧠 PERCEPTION NUKE ENGAGED.")
    apply_fake_artifacts()
    print("[+] Fake system hallucination deployed.")

if __name__ == "__main__":
    main()
