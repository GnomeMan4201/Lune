#!/usr/bin/env python3
# LUNE :: LureState Beacon
# Author: NMAPKin

import time
import random
from nmapkin_utils import banner, print_status, log_event

LOOP_COUNT = 5
LURE_MESSAGES = [
    "Operator ping received.",
    "LURE active — decoy responding.",
    "Heartbeat received from shell.",
    "Recon data sync complete.",
    "Operator is masked behind shell facade."
]

def emit_beacons():
    for _ in range(LOOP_COUNT):
        msg = random.choice(LURE_MESSAGES)
        log_event(msg)
        time.sleep(2)

def main():
    banner("LUNE :: LureState")
    print_status("Beaconing to operator backend...")
    emit_beacons()
    print_status("Beacon loop complete.", "✓")

if __name__ == "__main__":
    main()
