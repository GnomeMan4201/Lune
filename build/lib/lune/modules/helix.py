import subprocess
import random
import time
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt

FAKE_PROCESSES = [
    ("apt-get update", 2),
    ("systemctl restart bluetooth", 1),
    ("journalctl --since yesterday", 3),
    ("whoami", 0.5),
    ("ping -c 1 8.8.8.8", 1),
    ("ls -la /etc", 1.5),
    ("nano ~/.bashrc", 2),
    ("du -sh ~/Downloads", 2),
    ("python3 -m venv dummyenv", 2),
    ("curl -s https://example.com", 1)
]

def run_fake_dna(count):
    print(f"[dim]Injecting {count} fake process traces...[/dim]")
    for _ in range(count):
        cmd, delay = random.choice(FAKE_PROCESSES)
        print(f"[green]$ {cmd}[/green]")
        try:
            subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(delay)
        except Exception as e:
            print(f"[red]Error executing {cmd}: {e}[/red]")

def run():
    print(Panel("🧬 [bold magenta]HELIX — Process DNA Imprint Spoofer[/bold magenta]"))
    count = Prompt.ask("[cyan]Number of fake ops to run[/cyan]", default="6")
    try:
        run_fake_dna(int(count))
    except ValueError:
        print("[red]Please enter a valid number.[/red]")

def main(args=None):
    print("[helix] 🧬 Spoofing fake ops...")

if __name__ == "__main__":
    main()
