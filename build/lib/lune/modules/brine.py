import os
import subprocess
import random
from rich import print, panel

def random_mac():
    return "02:%02x:%02x:%02x:%02x:%02x" % tuple(random.randint(0x00, 0xff) for _ in range(5))

def run():
    print(panel.Panel("🌊 [bold cyan]BRINE[/bold cyan] — MAC Cloaker + History Purger"))
    iface = "wlan0"
    try:
        subprocess.run(["sudo", "ip", "link", "set", iface, "down"], check=True)
        new_mac = random_mac()
        subprocess.run(["sudo", "ip", "link", "set", iface, "address", new_mac], check=True)
        subprocess.run(["sudo", "ip", "link", "set", iface, "up"], check=True)
        os.system("sudo rm -f /etc/NetworkManager/system-connections/*")
        print(f"[green]MAC changed to {new_mac} and history wiped[/green]")
    except Exception as e:
        print(f"[red]Brine error:[/red] {e}")


main = run
