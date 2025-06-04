# vanish.py — Cleanup & Burn Module
import os
import subprocess
from rich import print, panel

def shred(path):
    try:
        subprocess.run(["shred", "-u", path], stderr=subprocess.DEVNULL)
        print(f"[dim]Shredded:[/dim] {path}")
    except:
        pass

def kill_artifacts():
    logs = ["/tmp/fake_audit.log", "/var/log/scan_report.txt"]
    cron_path = "/tmp/.lune"
    for path in logs + [cron_path]:
        if os.path.exists(path):
            shred(path)

    try:
        cron = subprocess.getoutput("crontab -l")
        lines = [line for line in cron.splitlines() if "/tmp/.lune" not in line]
        subprocess.run("crontab -", input="\n".join(lines).encode(), shell=True)
        print("[green]Cron cleaned.[/green]")
    except:
        pass

def nuke_suite():
    root = os.path.abspath(os.path.dirname(__file__))
    print("[red]Nuking entire suite from:[/red]", root)
    subprocess.run(["rm", "-rf", root])

def run():
    print(panel.Panel("\U0001F525 [bold red]VANISH[/bold red] — Erase, Obfuscate, Exit"))
    kill_artifacts()
    choice = input("[!] Full suite self-delete? (y/N): ").strip().lower()
    if choice == "y":
        nuke_suite()