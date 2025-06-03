import os
import json

TAG_DB_PATH = "/tmp/.lune_perception_tags.json"
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def list_tagged_directory(path):
    try:
        with open(TAG_DB_PATH, "r") as f:
            tags = json.load(f)
    except FileNotFoundError:
        tags = {}

    abs_path = os.path.abspath(os.path.expanduser(path))
    for file in os.listdir(abs_path):
        full_path = os.path.join(abs_path, file)
        display = file
        if full_path in tags:
            if tags[full_path]["real"]:
                print(f"{GREEN}🟩 {display}{RESET}")
            else:
                print(f"{RED}🟥 {display}{RESET}")
        else:
            print(f"{GREEN}🟩 {display}{RESET}")

def main():
    print("🔍 Operator Lens Activated. Viewing ~/Downloads")
    list_tagged_directory("~/Downloads")

if __name__ == "__main__":
    main()
