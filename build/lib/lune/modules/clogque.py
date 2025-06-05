import time
import importlib
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt

def delayed_run(module_name: str, delay_sec: int):
    print(f"[dim]Waiting {delay_sec} seconds before executing [cyan]{module_name}[/cyan]...[/dim]")
    time.sleep(delay_sec)

    try:
        mod = importlib.import_module(f"modules.{module_name}")
        if hasattr(mod, "run"):
            print(f"[green]→ Executing:[/green] {module_name}")
            mod.run()
        else:
            print(f"[red]Module '{module_name}' has no run() function.[/red]")
    except Exception as e:
        print(f"[red]Failed to run '{module_name}':[/red] {e}")

def run():
    print(Panel("⏱️ [bold magenta]CLOQUE — Time-Delayed Module Trigger[/bold magenta]"))

    mod = Prompt.ask("[cyan]Module to trigger[/cyan]")
    delay = Prompt.ask("[yellow]Delay in seconds[/yellow]", default="10")

    try:
        delay_sec = int(delay)
        delayed_run(mod, delay_sec)
    except ValueError:
        print("[red]Invalid delay value. Must be an integer.[/red]")

def main(args=None):
    print("[clogque] ⏱️ Simulating delayed module trigger.")
    print("Usage: clogque <module_name> <seconds>")

if __name__ == "__main__":
    main()
