#!/usr/bin/env python3
# LUNE :: (Deprecated) Legacy UI Launcher
# Author: NMAPKin

import os
import subprocess
from nmapkin_utils import banner, print_status, prompt_menu

LEGACY_MODULES = {
    "Fake Shell": "lune.py",
    "Fracture": "modules/fracture.py",
    "GhostLoad": "modules/ghostload.py",
    "LureState": "modules/lurestate.py",
    "Decoys": "modules/decoy.py"
}

def launch(path):
    if os.path.exists(path):
        print_status(f"Running: {path}")
        subprocess.run(["python3", path])
    else:
        print_status(f"Script not found: {path}", "✗")

def main():
    banner("LUNE :: Legacy UI")
    while True:
        choice = prompt_menu(list(LEGACY_MODULES.keys()) + ["Exit"])
        if choice == len(LEGACY_MODULES) + 1:
            print_status("Goodbye.", "✓")
            break
        elif 1 <= choice <= len(LEGACY_MODULES):
            launch(LEGACY_MODULES[list(LEGACY_MODULES.keys())[choice - 1]])
        else:
            print_status("Invalid option", "!")

if __name__ == "__main__":
    main()
