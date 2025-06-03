import os
import shutil
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt

def clean_bash_history():
    history_path = os.path.expanduser("~/.bash_history")
    if os.path.exists(history_path):
        with open(history_path, "w") as f:
            f.write("# cleaned by wallflower\n")
        print("[green]Bash history wiped.[/green]")
    else:
        print("[yellow]No bash history found.[/yellow]")

def clean_terminal_scrollback():
    print("\033c", end="")  # ANSI clear screen + scrollback
    print("[green]Terminal scrollback cleared.[/green]")

def list_recent_modifications(path="/tmp"):
    print(f"[cyan]Listing modified files in:[/cyan] {path}")
    os.system(f"find {path} -type f -printf '%TY-%Tm-%Td %TT %p\n' | sort -r | head -n 10")

def run():
    print(Panel("🌸 [bold magenta]WALLFLOWER — Trace Suppression & Activity Scrub[/bold magenta]"))

    choice = Prompt.ask(
        "[yellow]Choose action[/yellow]",
        choices=["bash_wipe", "scroll_clear", "recent", "all", "exit"],
        default="all"
    )

    if choice in ["bash_wipe", "all"]:
        clean_bash_history()

    if choice in ["scroll_clear", "all"]:
        clean_terminal_scrollback()

    if choice in ["recent", "all"]:
        list_recent_modifications()

def main(args=None):
    print("[wallflower] 🌸 Background noise injection stub.")

if __name__ == "__main__":
    main()
