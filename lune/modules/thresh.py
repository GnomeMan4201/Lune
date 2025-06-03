import os, socket, platform, shutil, json
from rich import print, panel

def check_processes(keywords):
    hits = []
    for proc in os.listdir('/proc'):
        if proc.isdigit():
            try:
                with open(f"/proc/{proc}/cmdline", "r") as f:
                    cmd = f.read().lower()
                    if any(keyword in cmd for keyword in keywords):
                        hits.append((proc, cmd))
            except:
                continue
    return hits

def run():
    print(panel.Panel("🔬 [bold green]THRESH[/bold green] — AV/EDR Scan"))
    tools = ["wireshark", "tcpdump", "avast", "eset", "carbonblack", "crowdstrike", "sysmon", "sandbox", "vmtoolsd", "vboxservice", "procmon", "tracer", "auditd"]
    found = {"tools": [t for t in tools if shutil.which(t)], "suspicious_procs": check_processes(tools)}
    print(json.dumps(found, indent=4))


main = run
