# shellsworn.py — Evasion using stealth-linked process name shifting
import importlib.util
from rich import print, panel

def load_stealth():
    spec = importlib.util.spec_from_file_location("stealth", "modules/stealth.py")
    stealth = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(stealth)
    return stealth

def run():
    print(panel.Panel("🐚 [bold red]SHELLSWORN[/bold red] — Linked Evasion Routine"))
    try:
        stealth = load_stealth()
        stealth.run()
        print("[green]Stealth module executed via Shellsworn[/green]")
    except Exception as e:
        print(f"[red]Shellsworn failed:[/red] {e}")