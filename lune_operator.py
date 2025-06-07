#!/usr/bin/env python3
# lune_operator.py

import os
import sys
from persona_engine import PersonaEngine
from ghostsig import GhostSignature
from tripwire import TripwireMonitor
from hall_of_mirrors import HallOfMirrors
from blacknoise import BlackNoise
from loot_watcher import LootWatcher

def lune_banner(active_persona=None):
    print("\033[1;32m")
    print("┌" + "─" * 73 + "┐")
    print("│{:^73s}│".format("L U N E   O P E R A T O R"))
    print("│{:^73s}│".format("(Live Deception | Persona Engine | Attribution)"))
    print("├" + "─" * 73 + "┤")
    print("│{:^73s}│".format("Welcome to LUNE. You control the shadows. Nothing here is what it seems."))
    print("├" + "─" * 73 + "┤")
    print("│ {:<38s}│ {:<31s}│".format("[1]  Adversary Persona Engine",         "[5]  Hall of Mirrors"))
    print("│ {:<38s}│ {:<31s}│".format("[2]  GhostSignature (False IOC Forge)", "[6]  BlackNoise Generator"))
    print("│ {:<38s}│ {:<31s}│".format("[3]  Tripwire Monitor",                 "[7]  Loot Watcher"))
    print("│ {:<38s}│ {:<31s}│".format("[4]  Attribution Poisoner",             "[8]  Exit"))
    print("├" + "─" * 73 + "┤")
    ap = active_persona if active_persona else "None (Select in option 1)"
    print(f"│  Active Persona:  {ap:<57s}│")
    print("└" + "─" * 73 + "┘\033[0m")

def main():
    persona_engine = PersonaEngine()
    ghostsig = GhostSignature()
    tripwire = TripwireMonitor()
    mirrors = HallOfMirrors()
    blacknoise = BlackNoise()
    lootwatch = LootWatcher()
    while True:
        os.system("clear")
        lune_banner(persona_engine.active_persona)
        try:
            choice = input("\nSelect an option: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n[!] Exiting LUNE.")
            break

        if choice == "1":
            persona_engine.select_persona()
        elif choice == "2":
            ghostsig.run(persona_engine.active_persona)
        elif choice == "3":
            tripwire.run()
        elif choice == "4":
            persona_engine.attribution_poisoning()
        elif choice == "5":
            mirrors.run(persona_engine.active_persona)
        elif choice == "6":
            blacknoise.run(persona_engine.active_persona)
        elif choice == "7":
            lootwatch.run()
        elif choice == "8":
            print("\n[!] Exiting LUNE. Stay unpredictable.")
            break
        else:
            print("[!] Invalid choice.")
        input("\n[Press Enter to return to menu]")

if __name__ == "__main__":
    main()
