import time
import random
import threading
import shutil
import os
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt

FAKE_COMMANDS = [
    "ls", "cd /tmp", "echo test", "touch temp.log",
    "cat /dev/null", "chmod +x run.sh", "curl -I example.com",
    "whoami", "ps aux | grep ssh", "clear"
]

def inject_noise(delay=2.5, count=10):
    print(f"[dim]Simulating {count} terminal inputs every {delay}s...[/dim]")
    for _ in range(count):
        cmd = random.choice(FAKE_COMMANDS)
        print(f"$ {cmd}")
        time.sleep(delay)

def toggle_capslock():
    if shutil.which("xdotool"):
        os.system("xdotool key Caps_Lock")
    else:
        print("[yellow]Capslock toggling requires 'xdotool' installed.[/yellow]")

def run():
    print(Panel("🪶 [bold magenta]GRACKLE — TTY Noise & Keystroke Ghoster[/bold magenta]"))

    mode = Prompt.ask("[cyan]Choose mode[/cyan]", choices=["noise", "capslock", "both"], default="noise")

    if mode in ["noise", "both"]:
        try:
            delay = float(Prompt.ask("[yellow]Delay between keystrokes (sec)[/yellow]", default="1.5"))
            count = int(Prompt.ask("[yellow]Number of commands to simulate[/yellow]", default="10"))
            inject_noise(delay, count)
        except ValueError:
            print("[red]Invalid input for delay or count[/red]")

    if mode in ["capslock", "both"]:
        print("[green]Toggling Caps Lock 5 times...[/green]")
        for _ in range(5):
            toggle_capslock()
            time.sleep(0.7)

def main(args=None):
    print("[grackle] 🪶 TTY Ghoster activated.")
    print("Use: grackle [noise|capslock|both]")

if __name__ == "__main__":
    main()
