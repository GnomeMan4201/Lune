
# lune-tui.py — LUNE Command Interface (with chaining support)
import os
import sys
import json
from pathlib import Path
from importlib import import_module
from rich import print
from rich.prompt import Prompt

MODULE_DIR = "modules"
CHAIN_FILE = Path("chain.json")

def list_modules():
    mods = sorted([f[:-3] for f in os.listdir(MODULE_DIR) if f.endswith(".py") and f != "__init__.py"])
    print("\n[+] Available modules:")
    for m in mods:
        print(f"    - {m}")

def run_module(module_name):
    try:
        mod = import_module(f"{MODULE_DIR}.{module_name}")
        print(f"\n▶️  Executing: {module_name}")
        mod.main()
        if CHAIN_FILE.exists():
            with open(CHAIN_FILE) as f:
                chain = json.load(f)
            if module_name in chain:
                for next_mod in chain[module_name]:
                    run_module(next_mod)
    except Exception as e:
        print(f"[!] Error running {module_name}: {e}")

def main():
    print("""\n
╔═════════════════════════════════════════════════════════╗
║   ██╗     ██╗   ██╗███╗   ██╗███████╗                   ║
║   ██║     ██║   ██║████╗  ██║██╔════╝   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀║
║   ██║     ██║   ██║██╔██╗ ██║█████╗     LUNE OPS SUITE ║
║   ██║     ██║   ██║██║╚██╗██║██╔══╝     passive + pivot║
║   ███████╗╚██████╔╝██║ ╚████║███████╗  curated modules ║
║   ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝  tui interface   ║
╚═════════════════════════════════════════════════════════╝
     > list        # see available tools
     > dryad xyz   # run passive recon on domain
     > exit        # quit the interface
""")
    while True:
        try:
            cmd = Prompt.ask("lune")
            if cmd.strip() == "exit":
                break
            elif cmd.strip() == "list":
                list_modules()
            else:
                parts = cmd.split()
                if len(parts) > 1:
                    run_module(parts[0])
                else:
                    run_module(cmd.strip())
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
