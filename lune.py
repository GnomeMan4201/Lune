#!/usr/bin/env python3
# LUNE :: Operator Shell Environment
# Author: NMAPKin

import os
import time
from nmapkin_utils import banner, print_status, log_event

FAKE_SHELL_PATH = "startup/fake_shell.sh"

def launch_fake_shell():
    if not os.path.exists(FAKE_SHELL_PATH):
        print_status("Fake shell script not found!", "✗")
        return
    print_status("Launching fake shell environment...")
    os.system(f"bash {FAKE_SHELL_PATH}")

def main():
    banner("LUNE :: False Reality Shell")
    print_status("Operator shell initialized")
    time.sleep(1)
    log_event("Simulating decoy terminal...")
    launch_fake_shell()

if __name__ == "__main__":
    main()
