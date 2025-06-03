import importlib
from rich import print
from rich.prompt import Prompt
from rich.panel import Panel

# All modules to allow chaining from
CHAINABLE = [
    "dryad", "fable", "relic", "noct", "vane", "palebox", "alibi", "wallflower"
]

def run_module(name):
    try:
        mod = importlib.import_module(f"modules.{name}")
        if hasattr(mod, "run"):
            print(f"\n[bold cyan]→ Running [green]{name}[/green][/bold cyan]")
            mod.run()
        else:
            print(f"[red]Module '{name}' has no run() function[/red]")
    except Exception as e:
        print(f"[red]Error loading module {name}:[/red] {e}")

def run():
    print(Panel("🧵 [bold magenta]CRUX — Chainable Module Orchestrator[/bold magenta]"))

    print("[bold cyan]Available modules:[/bold cyan]")
    for mod in CHAINABLE:
        print(f"  - {mod}")

    chain = Prompt.ask("\n[yellow]Enter modules to chain (space-separated)[/yellow]").strip().split()

    for mod_name in chain:
        if mod_name not in CHAINABLE:
            print(f"[red]Invalid module: {mod_name}[/red]")
            continue
        run_module(mod_name)

def main(args=None):
    print("[crux] 🧵 Chaining modules... (stub)")
    print("[crux] Run with: crux <mod1> <mod2> ...")

if __name__ == "__main__":
    main()
