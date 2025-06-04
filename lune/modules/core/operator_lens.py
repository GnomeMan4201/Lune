import os
import xattr

# Define the tag used for fake artifacts
FAKE_TAG = b"FAKE"

def is_fake(file_path):
    try:
        attrs = xattr.xattr(file_path)
        return attrs.get("user.fake") == FAKE_TAG
    except Exception:
        return False

def colorize(name, is_fake):
    return f"\033[91m{name}\033[0m" if is_fake else f"\033[92m{name}\033[0m"

def list_dir_filtered(path="."):
    try:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            tag = is_fake(full_path)
            print(colorize(item, tag))
    except Exception as e:
        print(f"[!] Failed to list directory: {e}")

if __name__ == "__main__":
    path = os.getcwd()
    print(f"[+] Operator Lens View — Directory: {path}")
    list_dir_filtered(path)
