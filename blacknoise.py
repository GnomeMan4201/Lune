# blacknoise.py
class BlackNoise:
    def run(self, persona):
        print("\033[1;36m\n[BlackNoise] Synthetic Network Traffic Generator")
        if not persona:
            print("[!] No persona selected. Run Persona Engine first.")
            return
        print(f"[*] Simulating outbound traffic for: {persona}")
        print("[+] DNS beacons, C2 callbacks, and lateral spray in progress.")
        input("\n[Press Enter to continue]\033[0m")
