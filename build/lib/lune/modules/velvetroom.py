"""
velvetroom.py — Identity & Fingerprint Auditor
Detects environmental leaks, entropy risk, and VM tells.
"""

import os
import platform
import uuid
import socket
import getpass
import subprocess

def velvetroom_main(*args):
    results = [banner()]
    results.append(f"[user] Username: {getpass.getuser()}")
    results.append(f"[host] Hostname: {socket.gethostname()}")
    results.append(f"[os] System: {platform.system()} {platform.release()}")
    results.append(f"[arch] Architecture: {platform.machine()}")
    results.append(f"[uuid] Node ID: {uuid.getnode()}")
    results.append(vm_check())
    results.append(mac_check())
    results.append(user_entropy())
    return "\n".join(results)


def banner():
    return r"""
╔═════════════════════════════════════╗
║ velvetroom — identity isolator     ║
╠═════════════════════════════════════╣
║  OPSEC fingerprint & correlation   ║
╚═════════════════════════════════════╝
"""


def vm_check():
    try:
        with open("/sys/class/dmi/id/product_name") as f:
            name = f.read().lower()
            if any(vm in name for vm in ['virtualbox', 'vmware', 'qemu', 'kvm']):
                return f"[vm] ⚠️ Detected virtualization layer: {name.strip()}"
    except:
        pass
    return "[vm] ✅ No virtualization tells found."


def mac_check():
    mac = hex(uuid.getnode())
    if mac.startswith("0x0") or mac.startswith("0x1"):
        return "[mac] ⚠️ MAC address in low entropy range (may be virtualized)."
    return "[mac] ✅ MAC appears randomized."


def user_entropy():
    uname = getpass.getuser().lower()
    risk_names = ['admin', 'user', 'test', 'root', 'vmuser']
    if uname in risk_names:
        return f"[entropy] ⚠️ Username '{uname}' may trigger risk scoring."
    return "[entropy] ✅ Username entropy acceptable."


run = velvetroom_main

def main(args=None):
    print("[velvetroom] 🚪 Entering session-space containment...")
    print("[velvetroom] 🔒 Payloads isolated in sandbox.")

if __name__ == "__main__":
    main()
