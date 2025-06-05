# glint.py — TLS Beacon with Covert Indicators
import time
import ssl
import socket
import random
from rich import print, panel

def fake_tls_beacon():
    host = "example.com"
    port = 443
    try:
        context = ssl.create_default_context()
        with socket.create_connection((host, port), timeout=3) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                ssock.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
                resp = ssock.recv(128)
                if resp:
                    print("[blue]Fake TLS beacon transmitted.[/blue]")
    except Exception as e:
        print(f"[red]Beacon failed:[/red] {e}")

def run():
    print(panel.Panel("\U0001F48E [bold blue]GLINT[/bold blue] — TLS Beacon Simulator"))
    interval = random.randint(5, 15)
    print(f"[dim]Sleeping {interval}s before beacon[/dim]")
    time.sleep(interval)
    fake_tls_beacon()


main = run
