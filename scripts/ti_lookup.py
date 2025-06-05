# Dummy threat intel lookup - to be expanded with AbuseIPDB or AlienVault OTX
import sys
import re

def extract_ips(text):
    return re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', text)

def main(filepath):
    with open(filepath, "r") as f:
        content = f.read()
    ips = extract_ips(content)
    print(f"[+] Found IPs: {ips} (not queried)")

if __name__ == "__main__":
    main(sys.argv[1])
