#!/usr/bin/env python3

import os
import platform
import socket
import getpass
import subprocess

def quick_recon():
    print("[LUNE] Recon sweep initiated...\n")

    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    user = getpass.getuser()
    system = platform.system()
    release = platform.release()
    distro = ' '.join(platform.uname())

    print(f"User      : {user}")
    print(f"Hostname  : {hostname}")
    print(f"IP Addr   : {ip}")
    print(f"System    : {system} {release}")
    print(f"Distro    : {distro}\n")

    try:
        uptime = subprocess.check_output("uptime -p", shell=True).decode().strip()
        print(f"Uptime    : {uptime}")
    except:
        pass

    print("\n[✔] Recon complete. Launching toolkit...\n")
    os.system("python3 lune-tui.py")

if __name__ == "__main__":
    quick_recon()
