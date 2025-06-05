import os
import ctypes
import platform
from rich import print
from rich.prompt import Prompt
from rich.panel import Panel

def set_proc_name(new_name: str):
    libc = ctypes.cdll.LoadLibrary("libc.so.6")
    result = libc.prctl(15, ctypes.create_string_buffer(new_name.encode()), 0, 0, 0)
    return result == 0

def run():
    print(Panel("🫥 [bold magenta]ALIBI — Process Masquerade Engine[/bold magenta]"))

    if platform.system() != "Linux":
        print("[red]Process renaming is only supported on Linux.[/red]")
        return

    current_pid = os.getpid()
    print(f"[cyan]Current PID:[/cyan] {current_pid}")

    new_name = Prompt.ask("[yellow]Spoof as (e.g. bash, cron, systemd)[/yellow]", default="bash")
    success = set_proc_name(new_name)

    if success:
        print(f"[green]Process name changed to:[/green] {new_name}")
        print(f"[dim]Check via: [italic]ps -p {current_pid} -o comm=[/italic][/dim]")
    else:
        print("[red]Failed to spoof process name. Root may be required.[/red]")

def main(args=None):
    print("[alibi] 🫥 Process Masquerade activated.")
    import os
    print(f"Current PID: {os.getpid()}")
    print("Check via: ps -p <pid> -o comm=")

if __name__ == "__main__":
    main()
