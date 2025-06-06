#!/usr/bin/env python3
# LUNE :: Decoy Injector
# Author: NMAPKin

import os
import json
from nmapkin_utils import banner, print_status, log_event

DECOY_FILE = "decoys.json"

def load_decoys():
    if not os.path.exists(DECOY_FILE):
        print_status(f"No decoy file found at {DECOY_FILE}", "✗")
        return []
    with open(DECOY_FILE, 'r') as f:
        return json.load(f)

def display_decoys(decoys):
    if not decoys:
        print_status("No decoys to display", "!")
        return
    for d in decoys:
        log_event(f"[{d.get('type')}] {d.get('ioc')} → {d.get('label', 'N/A')}")

def main():
    banner("LUNE :: Decoys")
    print_status("Loading decoys from file...")
    decoys = load_decoys()
    display_decoys(decoys)

if __name__ == "__main__":
    main()
