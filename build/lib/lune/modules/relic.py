import os
import shutil
import sqlite3
import platform
from pathlib import Path
from rich import print
from rich.table import Table

def chrome_history():
    path = Path.home() / ".config/google-chrome/Default/History"
    if not path.exists():
        path = Path.home() / ".config/chromium/Default/History"
    if not path.exists():
        return []

    tmp_copy = "/tmp/chrome_history.db"
    shutil.copy2(path, tmp_copy)

    urls = []
    try:
        conn = sqlite3.connect(tmp_copy)
        cursor = conn.cursor()
        cursor.execute("SELECT url, title, visit_count FROM urls ORDER BY visit_count DESC LIMIT 10;")
        urls = cursor.fetchall()
        conn.close()
        os.remove(tmp_copy)
    except Exception as e:
        print(f"[red]Failed to read Chrome history: {e}[/red]")
    return urls

def run():
    print("[bold magenta]🦴 RELIC — Local Forensics Extractor[/bold magenta]")

    print(f"[bold cyan]OS:[/bold cyan] {platform.system()} {platform.release()}")
    print(f"[bold cyan]User:[/bold cyan] {os.getlogin()}")

    # Chrome History
    history = chrome_history()
    if history:
        table = Table(title="Chrome/Chromium History", header_style="bold green")
        table.add_column("URL", overflow="fold")
        table.add_column("Title")
        table.add_column("Visits", justify="right")
        for url, title, visits in history:
            table.add_row(url, title, str(visits))
        print(table)
    else:
        print("[yellow]No Chrome/Chromium history found.[/yellow]")

    # Recently used files (Linux)
    recent = Path.home() / ".local/share/recently-used.xbel"
    if recent.exists():
        print(f"[bold cyan]Recent Files:[/bold cyan] {recent}")
    else:
        print("[dim]No recent file log found.[/dim]")

    # Mounted drives
    print("\n[bold cyan]Mounted Drives:[/bold cyan]")
    os.system("mount | grep ^/dev || echo 'No devices found.'")

def main(args=None):
    print("[relic] 🦴 Forensic extraction mode.")
    print("Analyzing local artifacts...")

if __name__ == "__main__":
    main()
