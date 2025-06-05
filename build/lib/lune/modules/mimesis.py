import os
import random
import subprocess
from rich import print
from rich.prompt import Prompt
from rich.panel import Panel

FAKE_BINARIES = [
    "dbus-daemon", "NetworkManager", "sshd", "systemd", "bash", "Xorg", "snapd", "modprobe"
]

FAKE_PINGS = [
    "curl -s https://www.google.com > /dev/null",
    "ping -c 1 github.com > /dev/null",
    "wget -q https://example.org",
    "nslookup localhost > /dev/null",
]

def rename_proc(fake_name):
    try:
        import ctypes
        libc = ctypes.cdll.LoadLibrary("libc.so.6")
        libc.prctl(15, fake_name.encode(), 0, 0, 0)
        print(f"[green]Process name set to:[/green] {fake_name}")
    except Exception as e:
        print(f"[red]Failed to spoof process name:[/red] {e}")

def fake_network_chatter():
    cmd = random.choice(FAKE_PINGS)
    subprocess.run(cmd, shell=True)
    print(f"[cyan]Ran spoofed network ping:[/cyan] {cmd}")

def run():
    print(Panel("🎭 [bold magenta]MIMESIS — Runtime Identity Spoof & Noise Layer[/bold magenta]"))

    fake = Prompt.ask("🧪 [yellow]Choose fake process name[/yellow]", choices=FAKE_BINARIES, default="sshd")
    rename_proc(fake)

    if Prompt.ask("🌐 Spoof network behavior? (y/n)", choices=["y", "n"], default="y") == "y":
        fake_network_chatter()

    print("[green]Mimesis layer applied. You're no longer yourself.[/green]")

def main(args=None):
    print("[mimesis] 🫣 Cloaking real identity...")
    print("[mimesis] Persona overlay active.")

if __name__ == "__main__":
    main()
