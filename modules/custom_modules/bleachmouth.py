import os
import re
import shutil
from rich import print, panel

TARGET_LOG = "/var/log/syslog"
CLEAN_COPY = "/tmp/bleached_syslog.log"
KEYWORDS = ["payload", "exploit", "reverse", "badBANANA", "lune", "rat", "inject"]

def sanitize_log(source, dest, keywords):
    if not os.path.exists(source):
        print(f"[red]Log file not found: {source}[/red]")
        return
    with open(source, "r", errors="ignore") as infile:
        lines = infile.readlines()
    pattern = re.compile("|".join(keywords), re.IGNORECASE)
    cleaned = [line for line in lines if not pattern.search(line)]
    with open(dest, "w") as outfile:
        outfile.writelines(cleaned)
    print(f"[green]Cleaned log written to:[/green] {dest}")

def run():
    print(panel.Panel("🧼 [bold cyan]BLEACHMOUTH[/bold cyan] — Log Sanitizer"))
    sanitize_log(TARGET_LOG, CLEAN_COPY, KEYWORDS)