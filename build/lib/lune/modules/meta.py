import os
import importlib
from pathlib import Path
from rich import print
from rich.table import Table

VERSION = "0.9.1"
MODULES_PATH = Path(__file__).parent
PROJECT_ROOT = MODULES_PATH.parent

def run():
    print(f"[bold cyan]LUNE Version:[/bold cyan] {VERSION}")
    print(f"[bold cyan]Project Root:[/bold cyan] {PROJECT_ROOT.resolve()}")
    print(f"[bold cyan]Modules Directory:[/bold cyan] {MODULES_PATH.resolve()}")

    table = Table(title="Module Health Check", header_style="bold magenta")
    table.add_column("Module", style="cyan")
    table.add_column("Status", style="green")

    for mod_file in MODULES_PATH.glob("*.py"):
        if mod_file.name == "__init__.py":
            continue
        mod_name = mod_file.stem
        try:
            mod = importlib.import_module(f"modules.{mod_name}")
            if hasattr(mod, "run"):
                table.add_row(mod_name, "[green]OK[/green]")
            else:
                table.add_row(mod_name, "[yellow]Missing run()[/yellow]")
        except Exception as e:
            table.add_row(mod_name, f"[red]Error: {e}[/red]")

    print(table)

def main(args=None):
    print("[meta] 🧠 Metadata synthesizer")

if __name__ == "__main__":
    main()
