# loot_watcher.py
import random
class LootWatcher:
    def run(self):
        print("\033[1;36m\n[Loot Watcher] Forensic Loot & Artifact Viewer")
        loot = [
            "Fake keylogger dump: 12,300 keystrokes (decoy)",
            "C2 IP logs: 198.51.100.34, 203.0.113.42",
            "Registry: HKLM\\Software\\Lazarus planted",
            "HR phishing email (artifact), not delivered"
        ]
        for item in loot:
            print(f"[+] {item}")
        input("\n[Press Enter to continue]\033[0m")
