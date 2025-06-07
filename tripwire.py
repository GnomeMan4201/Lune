# tripwire.py
import random
class TripwireMonitor:
    def run(self):
        print("\033[1;36m\n[Tripwire Monitor] Deception Triggers & Decoy Monitoring")
        events = [
            "Unauthorized PowerShell execution detected.",
            "Suspicious lateral movement (SMB relay) flagged.",
            "Decoy file modification in C:\\temp\\finance.xlsx",
            "Anomalous login from foreign IP."
        ]
        print(f"[+] {random.choice(events)}")
        print("[*] Tripwire log updated. (Viewable in loot_watcher)")
        input("\n[Press Enter to continue]\033[0m")

