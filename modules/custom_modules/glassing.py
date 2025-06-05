import platform, os, socket, subprocess
from rich import print, panel

def run():
    print(panel.Panel("🪟 [bold blue]GLASSING[/bold blue] — Recon Snapshot"))
    try:
        print(f"[green]Hostname:[/green] {socket.gethostname()}")
        print(f"[green]OS:[/green] {platform.system()} {platform.release()}")
        with open('/proc/uptime', 'r') as f:
            uptime = float(f.readline().split()[0])
            print(f"[green]Uptime:[/green] {int(uptime // 3600)} hours")
        who = subprocess.check_output("who", shell=True).decode().strip()
        print(f"[green]Users:[/green]\n{who if who else 'None'}")
        ip = subprocess.check_output("ip addr", shell=True).decode()
        for line in ip.split('\n'):
            if "inet " in line and "scope global" in line:
                print(f"[blue]{line.strip()}[/blue]")
        ps = subprocess.check_output("ps -eo pid,comm,%mem --sort=-%mem | head -n 6", shell=True).decode().strip()
        print(f"[green]Top Processes:[/green]\n{ps}")
    except Exception as e:
        print(f"[red]Glassing error:[/red] {e}")