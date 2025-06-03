import os
import hashlib

# Shared secret to recognize real files
REAL_TAG_SECRET = "lune_perception_schism"

def tag_file_as_real(path):
    tag = hashlib.sha256((path + REAL_TAG_SECRET).encode()).hexdigest()[:8]
    with open(path + ".tag", "w") as f:
        f.write(tag)

def is_file_real(path):
    tag_file = path + ".tag"
    if not os.path.exists(tag_file):
        return False
    with open(tag_file) as f:
        tag = f.read().strip()
    return tag == hashlib.sha256((path + REAL_TAG_SECRET).encode()).hexdigest()[:8]

def overlay_ls(path="."):
    print("[operatorlens] Overlay view of directory:")
    for fname in os.listdir(path):
        full_path = os.path.join(path, fname)
        if os.path.isfile(full_path):
            real = is_file_real(full_path)
            marker = "🟩" if real else "🟥"
            print(f"{marker} {fname}")

def overlay_cat(path):
    if is_file_real(path):
        print(f"[operatorlens] 🟩 REAL CONTENT of {path}:\n")
        with open(path) as f:
            print(f.read())
    else:
        print(f"[operatorlens] 🟥 FAKE OR UNTAGGED CONTENT of {path}:\n")
        with open(path) as f:
            print(f.read())

def main():
    print("[operatorlens] Try: overlay_ls() or overlay_cat('/path/to/file') inside this module.")

if __name__ == "__main__":
    main()
