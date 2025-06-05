import time
import json
import requests

DECOY_URLS = [
    "https://example-decoystorage.com/fake_token_1",
    "https://example-decoystorage.com/fake_env_2"
]

def log_access(ip, url):
    with open("docs/intel/tripwire_hits.log", "a") as log:
        log.write(f"{time.ctime()} - IP: {ip}, URL: {url}\n")

def simulate_listener():
    for url in DECOY_URLS:
        fake_ip = "203.0.113." + str(int(time.time()) % 255)
        print(f"[!] Decoy touched: {url} from {fake_ip}")
        log_access(fake_ip, url)
        time.sleep(1)

if __name__ == "__main__":
    print("[*] Tripwire Recon Monitor active...")
    simulate_listener()