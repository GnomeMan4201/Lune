import ssl
import socket
from rich import print, panel

def get_cert_info(hostname, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port), timeout=5) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            return cert

def run():
    print(panel.Panel("🪵 [bold magenta]ETCH[/bold magenta] — TLS Certificate Scanner"))
    host = input("Target domain/IP (TLS): ").strip()
    try:
        info = get_cert_info(host)
        print(f"[cyan]Subject:[/cyan] {info['subject']}")
        print(f"[cyan]Issuer:[/cyan] {info['issuer']}")
        print(f"[cyan]Valid From:[/cyan] {info['notBefore']} to {info['notAfter']}")
    except Exception as e:
        print(f"[red]ETCH failed:[/red] {e}")


main = run
