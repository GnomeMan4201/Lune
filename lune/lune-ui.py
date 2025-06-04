#!/usr/bin/env python3
import os
import sys
import importlib
from datetime import datetime
import platform
import psutil
import json
import argparse
import io
from contextlib import redirect_stdout, redirect_stderr

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

RED = "\033[91m"
RESET = "\033[0m"

BANNER = f"""{RED}
██╗     ██╗   ██╗███╗   ██╗███████╗
██║     ██║   ██║████╗  ██║██╔════╝
██║     ██║   ██║██╔██╗ ██║█████╗  
██║     ██║   ██║██║╚██╗██║██╔══╝  
███████╗╚██████╔╝██║ ╚████║███████╗
╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
{RESET}
 LUNE :: Offensive Operator Console
──────────────────────────────────────────────
"""

# Load module descriptions dynamically
MODULES = {}
module_desc_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "configs", "module_descriptions.json"))
with open(module_desc_path, 'r') as f:
    module_desc = json.load(f)
    MODULES = {k: (f"modules.{k}", v) for k, v in module_desc.items()}

# Prepare log directory
session_dir = os.path.join(os.path.dirname(__file__), '..', '.lune_sessions', datetime.now().strftime("%Y%m%d_%H%M%S"))
os.makedirs(session_dir, exist_ok=True)

def show_modules():
    print("\nAvailable Modules:")
    for idx, (mod, (path, desc)) in enumerate(MODULES.items(), 1):
        print(f" [{idx}] {mod:<20} - {desc}")

def execute_module(mod_name):
    mod_path = MODULES.get(mod_name, (None,))[0]
    if not mod_path:
        print("[!] Module not found.")
        return
    log_file = os.path.join(session_dir, f"{mod_name}.log")
    try:
        mod = importlib.import_module(mod_path)
        if hasattr(mod, 'run'):
            print(f"[+] Running {mod_name}...")
            with open(log_file, 'w') as f, redirect_stdout(f), redirect_stderr(f):
                mod.run()
            print(f"[✓] {mod_name} completed. Log saved to {log_file}")
        else:
            print("[-] No run() method found in module.")
    except Exception as e:
        print(f"[!] Failed to load module {mod_name}: {e}")

def run_chain(chain_path):
    try:
        with open(chain_path, 'r') as f:
            chain = json.load(f)
        for step in chain.get("modules", []):
            print(f"\n⏳ Executing chain module: {step}")
            execute_module(step)
    except Exception as e:
        print(f"[!] Failed to execute chain: {e}")

def quickstart():
    default_chain = ["stealth", "dreamtether", "fracture"]
    for mod in default_chain:
        print(f"\n🚀 Quickstart module: {mod}")
        execute_module(mod)

def main():
    parser = argparse.ArgumentParser(description="LUNE Operator Console")
    parser.add_argument('--quickstart', action='store_true', help='Run default quickstart module set')
    parser.add_argument('--chain', type=str, help='Path to chain JSON file')
    parser.add_argument('--list', action='store_true', help='List available modules')
    args = parser.parse_args()

    print(BANNER)

    if args.list:
        show_modules()
        return
    if args.quickstart:
        quickstart()
        return
    if args.chain:
        run_chain(args.chain)
        return

    show_modules()
    while True:
        choice = input("\nEnter module name to execute (or 'exit'): ").strip()
        if choice.lower() == 'exit':
            break
        execute_module(choice)

if __name__ == '__main__':
    main()
