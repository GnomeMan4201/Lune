# persona_engine.py

import random
import time
import os

PERSONAS = [
    {
        "name": "Lazarus Group (North Korea)",
        "ttps": [
            "DNS beacons to msupdate[.]co.kr",
            "Registry keys HKLM\\Software\\Lazarus",
            "PowerShell scripts in %TEMP%",
            "Fake dropper binaries"
        ]
    },
    {
        "name": "APT29 / Cozy Bear (Russia)",
        "ttps": [
            "Custom backdoors",
            "C2 traffic to known APT29 IPs",
            "Malicious DLL side-loading",
            "Logon scripts in startup folders"
        ]
    },
    {
        "name": "FIN7 (Financial Crime)",
        "ttps": [
            "Macro-laced Office docs",
            "Phishing emails to CFO",
            "Fake IT support chat artifacts",
            "POS malware signatures"
        ]
    },
    {
        "name": "Equation Group (NSA)",
        "ttps": [
            "Encrypted payloads in registry",
            "RC5 key artifacts",
            "Staged exploits in task scheduler",
            "Shadow Brokers C2 beacon"
        ]
    },
    {
        "name": "Sandworm (GRU)",
        "ttps": [
            "Wiper malware stubs",
            "Malware in System32",
            "Fake SCADA/ICS artifacts",
            "Industroyer traffic"
        ]
    },
    {
        "name": "Script Kiddie",
        "ttps": [
            "Public Metasploit payloads",
            "Obvious nmap logs",
            "Discord webhook spam",
            "Defacement HTML in webroot"
        ]
    },
]

class PersonaEngine:
    def __init__(self):
        self.persona = None
        self.active_persona = None
        self.deception_artifacts = []
        self.se_artifacts = []
        self.attribution_traces = []
        self.traffic_mirage = []
        self.cleaned = False

    def select_persona(self):
        os.system("clear")
        print("\033[1;32m")
        print("┌" + "─" * 57 + "┐")
        print("│{:^57s}│".format("ADVERSARY PERSONA ENGINE"))
        print("├" + "─" * 57 + "┤")
        print("│{:^57s}│".format("Select adversary persona:"))
        for idx, persona in enumerate(PERSONAS, 1):
            print(f"│  [{idx}] {persona['name']:<48s}│")
        print("│  [7] Random                                             │")
        print("└" + "─" * 57 + "┘\033[0m")
        choice = input("Select persona: ").strip()
        if choice == "7" or (not choice.isdigit()) or int(choice) not in range(1, 7+1):
            self.persona = random.choice(PERSONAS)
        else:
            self.persona = PERSONAS[int(choice)-1]
        self.active_persona = self.persona["name"]
        print(f"\n[✓] Persona selected: {self.active_persona}")
        print("TTPs and typical IOCs:")
        for ttp in self.persona["ttps"]:
            print(f"  - {ttp}")
        input("\n[Press Enter to continue]")

    def inject_social_engineering(self):
        os.system("clear")
        if not self.persona:
            print("[!] Select an adversary persona first (Option 1).")
            return
        print(f"[+] Injecting social engineering payloads for {self.active_persona}...")
        self.se_artifacts = [
            f"Phishing email from {self.active_persona} persona",
            f"HR memo artifact",
            f"Fake CEO wire transfer request"
        ]
        for artifact in self.se_artifacts:
            print(f"  - {artifact}")
            time.sleep(0.5)
        print("[✓] Social engineering artifacts injected.")

    def deploy_live_deception(self):
        os.system("clear")
        if not self.persona:
            print("[!] Select an adversary persona first (Option 1).")
            return
        print(f"[+] Deploying live deception overlay for {self.active_persona}...")
        self.deception_artifacts = []
        for ttp in self.persona["ttps"]:
            artifact = f"Simulated: {ttp}"
            self.deception_artifacts.append(artifact)
            print(f"  [✓] {artifact}")
            time.sleep(0.4)
        print("[✓] Deception overlay complete.")

    def attribution_poisoning(self):
        os.system("clear")
        if not self.persona:
            print("[!] Select an adversary persona first (Option 1).")
            return
        print(f"[+] Running attribution poisoning for {self.active_persona}...")
        self.attribution_traces = [
            f"Log entry referencing {self.active_persona}",
            f"Registry marker: {self.active_persona.split()[0]}",
            f"Fake indicator: C2 beacon (persona)"
        ]
        for trace in self.attribution_traces:
            print(f"  - {trace}")
            time.sleep(0.4)
        print("[✓] Attribution artifacts in place.")

    def traffic_signal_mirage(self):
        os.system("clear")
        if not self.persona:
            print("[!] Select an adversary persona first (Option 1).")
            return
        print(f"[+] Simulating adversary traffic for {self.active_persona}...")
        self.traffic_mirage = [
            f"DNS beacon to {self.active_persona.split()[0].lower()}-c2.example.net",
            f"Random outbound packet to staged IP"
        ]
        for t in self.traffic_mirage:
            print(f"  - {t}")
            time.sleep(0.3)
        print("[✓] Traffic signal mirage complete.")

    def artifact_cleanup(self):
        os.system("clear")
        self.deception_artifacts = []
        self.se_artifacts = []
        self.attribution_traces = []
        self.traffic_mirage = []
        self.cleaned = True
        print("[✓] All deception and persona artifacts cleaned up.")

    def generate_dfir_report(self):
        os.system("clear")
        print("\033[1;32m")
        print("┌" + "─" * 57 + "┐")
        print("│{:^57s}│".format("DFIR ANALYST REPORT"))
        print("├" + "─" * 57 + "┤")
        print(f"│ Persona: {self.active_persona or 'None':<47s}│")
        print("│ Deception Artifacts:                                  │")
        for a in self.deception_artifacts:
            print(f"│   • {a:<50s}│")
        print("│ Social Engineering Payloads:                          │")
        for s in self.se_artifacts:
            print(f"│   • {s:<50s}│")
        print("│ Attribution Traces:                                   │")
        for t in self.attribution_traces:
            print(f"│   • {t:<50s}│")
        print("│ Traffic Mirage:                                       │")
        for t in self.traffic_mirage:
            print(f"│   • {t:<50s}│")
        print("│                                                      │")
        print(f"│ Attribution: Strong match for {self.active_persona or 'None':<24s}│")
        print("└" + "─" * 57 + "┘\033[0m")
        input("\n[Press Enter to continue]")

