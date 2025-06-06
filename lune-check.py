#!/usr/bin/env python3
# LUNE :: Diagnostic Checker
# Author: NMAPKin

import os
import importlib.util
from nmapkin_utils import banner, print_status

MODULES = [
    "modules/decoy.py",
    "modules/etch.py",
    "modules/fracture.py",
    "modules/ghostload.py",
    "modules/lurestate.py",
    "nmapkin_utils.py",
    "lune.py",
    "lune-launcher.py"
]

def check_main(path):
    try:
        with open(path) as f:
            return "def main" in f.read()
    except:
        return False

def check_imports(module):
    spec = importlib.util.spec_from_file_location("mod", module)
    try:
        importlib.util.module_from_spec(spec)
        return True
    except:
        return False

def run_diagnostics():
    for m in MODULES:
        if not os.path.exists(m):
            print_status(f"{m} :: Missing", "✗")
        elif not check_main(m):
            print_status(f"{m} :: Missing main()", "!")
        elif not check_imports(m):
            print_status(f"{m} :: ImportError", "-")
        else:
            print_status(f"{m} :: OK", "✓")

def main():
    banner("LUNE :: Self-Diagnostic")
    print_status("Running integrity checks...")
    run_diagnostics()

if __name__ == "__main__":
    main()
