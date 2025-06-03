import os
import subprocess
import platform
from datetime import datetime
from pathlib import Path
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt

def screenshot(out_path="screenshot.png"):
    system = platform.system()
    try:
        if system == "Linux":
            subprocess.run(["import", "-window", "root", out_path])
        elif system == "Darwin":
            subprocess.run(["screencapture", out_path])
        elif system == "Windows":
            from PIL import ImageGrab
            img = ImageGrab.grab()
            img.save(out_path)
        else:
            print("[red]Unsupported OS for screenshot[/red]")
            return False
        return True
    except Exception as e:
        print(f"[red]Screenshot failed:[/red] {e}")
        return False

def clipboard_read():
    system = platform.system()
    try:
        if system == "Linux":
            return subprocess.check_output(["xclip", "-selection", "clipboard", "-o"]).decode()
        elif system == "Darwin":
            return subprocess.check_output("pbpaste").decode()
        elif system == "Windows":
            import pyperclip
            return pyperclip.paste()
        else:
            return ""
    except Exception:
        return "[dim italic]Clipboard unavailable or unsupported[/dim italic]"

def run():
    print(Panel("🖼️ [bold magenta]MIRADOR — Screenshot & Clipboard Intel[/bold magenta]"))

    time_now = datetime.now().strftime("%Y%m%d-%H%M%S")
    save_dir = Path("output")
    save_dir.mkdir(exist_ok=True)
    shot_file = save_dir / f"screenshot-{time_now}.png"

    print("[cyan]Attempting screenshot...[/cyan]")
    if screenshot(str(shot_file)):
        print(f"[green]Saved:[/green] {shot_file}")
    else:
        print("[red]Screenshot failed or tool not installed.[/red]")
        print("[yellow]Tip: Linux needs 'imagemagick' (import), Windows needs Pillow.[/yellow]")

    clip = clipboard_read()
    print("\n[bold]Clipboard Content:[/bold]")
    print(f"[dim]{clip}[/dim]")

def main(args=None):
    print("[mirador] 👁️ Launching remote sight routine.")

if __name__ == "__main__":
    main()
