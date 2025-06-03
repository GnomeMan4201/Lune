import builtins
import socket
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt

# Store original references
_original_open = open
_original_socket = socket.socket

# Hooked open()
def hooked_open(*args, **kwargs):
    print(f"[dim]Intercepted open():[/dim] [yellow]{args[0]}[/yellow]")
    return _original_open(*args, **kwargs)

# Hooked socket()
class HookedSocket(socket.socket):
    def connect(self, address):
        print(f"[dim]Intercepted connect():[/dim] [cyan]{address}[/cyan]")
        return super().connect(address)

def install_hooks():
    builtins.open = hooked_open
    socket.socket = HookedSocket
    print("[green]Runtime hooks installed into 'open' and 'socket.connect'.[/green]")

def test_hooks():
    print("[bold]→ Testing open()[/bold]")
    with open("/etc/hostname", "r") as f:
        f.read()

    print("[bold]→ Testing socket connect()[/bold]")
    s = socket.socket()
    try:
        s.connect(("example.com", 80))
    except Exception:
        pass

def run():
    print(Panel("🧵 [bold magenta]SLIPHOOK — In-Memory Function Interceptor[/bold magenta]"))

    install_hooks()
    confirm = Prompt.ask("[cyan]Run built-in test sequence?[/cyan]", choices=["yes", "no"], default="yes")

    if confirm == "yes":
        test_hooks()

def main(args=None):
    print("[sliphook] 🪝 Covert listener initialized.")

if __name__ == "__main__":
    main()
