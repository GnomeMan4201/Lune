# ghostsig.py
class GhostSignature:
    def run(self, persona):
        print("\033[1;36m\n[GhostSignature] False Indicator of Compromise Generator")
        if not persona:
            print("[!] No persona selected. Run Persona Engine first.")
            return
        print(f"[*] Forging IOC patterns linked to: {persona}")
        print(f"[+] Fake C2 IPs, Registry keys, and malware hashes injected for {persona}.")
        input("\n[Press Enter to continue]\033[0m")
