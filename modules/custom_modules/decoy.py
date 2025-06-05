# decoy.py — Analyst Deception Layer
import os
from rich import print, panel

def drop_fake_logs():
    paths = ["/tmp/fake_audit.log", "/var/log/scan_report.txt"]
    content = "[!] Unauthorized access detected\nIP: 127.0.0.1\nTool: metasploit\n" * 3
    for path in paths:
        try:
            with open(path, "w") as f:
                f.write(content)
            print(f"[dim]Decoy dropped:[/dim] {path}")
        except:
            pass

def run():
    print(panel.Panel("\U0001F6E1 [bold yellow]DECOY[/bold yellow] — Mislead & Obfuscate"))
    drop_fake_logs()
    print("[green]Analyst confusion engaged.[/green]")