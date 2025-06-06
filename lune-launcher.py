#!/usr/bin/env python3
# LUNE :: Launcher Interface
# Author: NMAPKin

import os
import subprocess
from nmapkin_utils import banner, print_status, prompt_menu

MODULES = {
    "Run Fake Shell": "lune.py",
    "LUNE Self-Diagnostic": "lune-check.py",
    "View Decoys": "modules/decoy.py",
    "Trigger Artifacts": "modules/etch.py",
    "Inject Fractures": "modules/fracture.py",
    "Ghostload Engine": "modules/ghostload.py",
    "Lurestate Tracker": "modules/lurestate.py"
}

def run_script(path):
    if not os.path.exists(path):
        print_status(f"Script not found: {path}", "✗")
        return
    print_status(f"Executing: {path}")
    subprocess.run(["python3", path])

def main():
    banner("LUNE :: Red Team Deception")
    while True:
        choice = prompt_menu(list(MODULES.keys()) + ["Exit"])
        if choice == len(MODULES) + 1:
            print_status("Exiting LUNE.", "✓")
            break
        elif 1 <= choice <= len(MODULES):
            label = list(MODULES.keys())[choice - 1]
            run_script(MODULES[label])
        else:
            print_status("Invalid selection", "!")

if __name__ == "__main__":
    main()
