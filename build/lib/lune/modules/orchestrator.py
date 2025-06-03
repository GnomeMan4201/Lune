import os
import importlib
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

CHAIN = []
console = Console()

def show_chain():
    table = Table(title="Current Execution Chain")
    table.add_column("#", style="cyan", justify="right")
    table.add_column("Module", style="magenta")
    for i, m in enumerate(CHAIN):
        table.add_row(str(i + 1), m)
    console.print(table)

def add_module():
    module = Prompt.ask("[green]+ Add module to chain")
    try:
        importlib.import_module(f"modules.{module}")
        CHAIN.append(module)
        console.print(f"[green][+][/green] Module [bold]{module}[/bold] added.")
    except ImportError:
        console.print(f"[red][-][/red] Module '{module}' not found.")

def remove_module():
    show_chain()
    idx = Prompt.ask("❌ Index to remove", default="0")
    try:
        removed = CHAIN.pop(int(idx) - 1)
        console.print(f"[yellow][-] Removed {removed} from chain.[/yellow]")
    except:
        console.print("[red]Invalid index.[/red]")

def run_chain():
    if not CHAIN:
        console.print("[red][-] No modules in chain to run.[/red]")
        return
    for mod in CHAIN:
        console.print(f"\n[bold blue]>>> Running {mod}[/bold blue]")
        try:
            m = importlib.import_module(f"modules.{mod}")
            if hasattr(m, "run"):
                m.run()
            else:
                console.print(f"[red]![/red] Module '{mod}' has no run()")
        except Exception as e:
            console.print(f"[red]Error in {mod}: {e}[/red]")

def save_chain():
    with open("chain.lune", "w") as f:
        for m in CHAIN:
            f.write(f"{m}\n")
    console.print("[cyan][✓] Chain saved as chain.lune[/cyan]")

def load_chain():
    if not os.path.exists("chain.lune"):
        console.print("[red][-] No saved chain found.[/red]")
        return
    with open("chain.lune") as f:
        lines = f.read().splitlines()
        for m in lines:
            CHAIN.append(m)
    console.print("[green][+] Loaded saved chain.[/green]")

def reset_chain():
    CHAIN.clear()
    console.print("[yellow][!] Chain reset.[/yellow]")

def run():
    console.print(Panel("🤖 [bold cyan]LUNE Orchestrator[/bold cyan] — Chain Modules, Build Flows, Dominate"))
    while True:
        cmd = Prompt.ask("[orchestrator] > ", choices=["add", "remove", "show", "run", "save", "load", "reset", "exit"])
        if cmd == "add": add_module()
        elif cmd == "remove": remove_module()
        elif cmd == "show": show_chain()
        elif cmd == "run": run_chain()
        elif cmd == "save": save_chain()
        elif cmd == "load": load_chain()
        elif cmd == "reset": reset_chain()
        elif cmd == "exit": break

def main(args=None):
    print("[orchestrator] 🔧 Build your session chain...")
    print("Stub operational.")

if __name__ == "__main__":
    main()
