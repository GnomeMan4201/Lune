# stealth.py — Process Name Spoofer
import ctypes
import sys
from rich import print, panel, prompt

def spoof_name(new_name):
    libc = ctypes.cdll.LoadLibrary("libc.so.6")
    buff = ctypes.create_string_buffer(len(new_name) + 1)
    buff.value = new_name.encode('utf-8')
    libc.prctl(15, ctypes.byref(buff), 0, 0, 0)
    print(f"[blue]Process name spoofed to:[/blue] {new_name}")

def run():
    print(panel.Panel("\U0001F575 [bold cyan]STEALTH[/bold cyan] — Process Masquerade Engine"))
    try:
        current = sys.argv[0]
        print(f"[dim]Current: {current}[/dim]")
        new_name = prompt.Prompt.ask("Spoof as (e.g. bash, cron, systemd)", default="bash")
        spoof_name(new_name)
    except Exception as e:
        print(f"[red]Stealth error:[/red] {e}")