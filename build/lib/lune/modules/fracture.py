# fracture.py — Time Skew Attack
import os
import subprocess
import time
from rich import print, panel

def skew_time_by_ntp(server="0.pool.ntp.org"):
    try:
        subprocess.run(["ntpdate", server], check=True)
        print(f"[green]Time updated via {server}[/green]")
    except Exception as e:
        print(f"[red]NTP sync failed:[/red] {e}")

def skew_time_by_offset(offset_days=7):
    try:
        future = time.time() + offset_days * 86400
        os.system(f"date -s '@{int(future)}'")
        print(f"[green]System time skewed by {offset_days} days[/green]")
    except Exception as e:
        print(f"[red]Manual skew failed:[/red] {e}")

def run():
    print(panel.Panel("\U0001F50C [bold red]FRACTURE[/bold red] — Time Skew Attack"))
    choice = input("Skew via [ntp/manual]? ").strip().lower()
    if choice == "ntp":
        skew_time_by_ntp()
    elif choice == "manual":
        skew_time_by_offset()
    else:
        print("[yellow]Invalid choice[/yellow]")


main = run
