import os
import random
import string
from pathlib import Path
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt

FAKE_DIRS = ["logs", "temp", "cache", "configs", "scripts", "archive"]
FAKE_EXTS = [".log", ".txt", ".sh", ".conf", ".ini"]
DECOY_NAMES = [
    "session_dump", "audit_trace", "userprefs", "launchd_backup", "policy_sync", "job_watchdog"
]

def random_text(length=256):
    return ''.join(random.choices(string.ascii_letters + string.digits + ' \n', k=length))

def make_mirage(base_dir="decoy_mirage", depth=3, files_per=6):
    base_path = Path(base_dir)
    base_path.mkdir(exist_ok=True)
    print(f"[dim]Creating decoy environment at:[/dim] {base_path.resolve()}")

    for level in range(depth):
        for _ in range(3):  # subdirs per level
            dname = random.choice(FAKE_DIRS)
            sub_path = base_path / "/".join([f"{dname}_{level}_{i}" for i in range(random.randint(1, 2))])
            sub_path.mkdir(parents=True, exist_ok=True)

            for _ in range(files_per):
                fname = random.choice(DECOY_NAMES) + random.choice(FAKE_EXTS)
                fpath = sub_path / fname
                with open(fpath, "w") as f:
                    if fpath.suffix in [".log", ".txt"]:
                        f.write(random_text(512))
                    else:
                        f.write("# config file\n")

    print("[green]Fake filesystem deployed.[/green]")

def run():
    print(Panel("🪞 [bold magenta]OBSCURA — Filesystem Mirage Generator[/bold magenta]"))
    target = Prompt.ask("[cyan]Target directory name[/cyan]", default="decoy_mirage")
    make_mirage(target)

def main(args=None):
    print("[obscura] 🖤 Obfuscation mode enabled.")
    print("Payloads masked.")

if __name__ == "__main__":
    main()
