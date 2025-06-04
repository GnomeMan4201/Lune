
# pivot.py — Lateral Movement Toolkit
import os
import socket
import subprocess
from getpass import getuser
from rich import print, panel, prompt

def discover_network():
    print("[cyan]Scanning local subnet for alive hosts...[/cyan]")
    subnet = socket.gethostbyname(socket.gethostname()).rsplit('.', 1)[0] + '.'
    hosts = []
    for i in range(1, 255):
        ip = f"{subnet}{i}"
        result = subprocess.run(["ping", "-c", "1", "-W", "1", ip], stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            hosts.append(ip)
    return hosts

def scan_services(ip):
    open_ports = []
    for port in [22, 445, 3389]:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            sock.connect((ip, port))
            open_ports.append(port)
        except:
            pass
        sock.close()
    return open_ports

def attempt_ssh(ip, user, key_path):
    test_cmd = ["ssh", f"{user}@{ip}", "echo", "PIVOT_SUCCESS"]
    result = subprocess.run(test_cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    if b"PIVOT_SUCCESS" in result.stdout:
        print(f"[green]SSH access confirmed to {ip}[/green]")
        return True
    return False

def run():
    print(panel.Panel("\U0001F5A5 [bold green]PIVOT[/bold green] — Lateral Movement Toolkit"))
    user = prompt.Prompt.ask("SSH username", default=getuser())
    key_path = prompt.Prompt.ask("SSH key path", default=os.path.expanduser("~/.ssh/id_rsa"))

    hosts = discover_network()
    print(f"[bold]Alive Hosts:[/bold] {hosts}")

    for ip in hosts:
        ports = scan_services(ip)
        if 22 in ports:
            print(f"[yellow]{ip}[/yellow] - Attempting SSH login...")
            os.environ["SSH_AUTH_SOCK"] = "/tmp/agent.sock"
            if attempt_ssh(ip, user, key_path):
                print(f"[green]Pivot access to {ip} confirmed.[/green]")
    print("[green]Lateral movement check complete.[/green]")
