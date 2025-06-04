import os
import re

# Map of hallucinated → real mappings
FILENAME_MAP = {
    "cmd_exec_history.txt": "client_report.md",
    "api_keys_leaked.json": "env_config.json",
    "wallet_seed.png": "profile_pic.png",
    "server_backup_03.bak": "meeting_notes.txt"
}

def hallucinate_view(entries):
    # Normal user sees fake filenames
    return list(FILENAME_MAP.keys())

def traitor_view(entries):
    # Operator sees true filenames
    return [FILENAME_MAP.get(e, e) for e in entries]

def list_files(user="traitor"):
    entries = os.listdir()
    if user == "traitor":
        view = traitor_view(entries)
    else:
        view = hallucinate_view(entries)

    for item in view:
        print(item)

if __name__ == "__main__":
    print("=== Trait View ===")
    list_files("traitor")
    print("\n=== Hallucinated View ===")
    list_files("user")
