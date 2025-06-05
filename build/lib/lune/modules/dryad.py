import socket
import whois
import dns.resolver
from rich import print
from rich.panel import Panel

def run():
    print(Panel("🌿 [bold green]DRYAD[/bold green] — Passive Recon & Domain Fingerprinting", style="green"))
    domain = input("[bold cyan]Enter domain (no http/https): [/bold cyan]").strip()

    if not domain:
        print("[red]No domain provided.[/red]")
        return

    try:
        ip = socket.gethostbyname(domain)
        print(f"[bold yellow]Resolved IP:[/bold yellow] {ip}")
    except Exception as e:
        print(f"[red]DNS resolution failed: {e}[/red]")
        return

    try:
        w = whois.whois(domain)
        print(f"[bold green]WHOIS Lookup:[/bold green]")
        print(f"  [cyan]Registrar:[/cyan] {w.registrar}")
        print(f"  [cyan]Created:[/cyan] {w.creation_date}")
        print(f"  [cyan]Expires:[/cyan] {w.expiration_date}")
        print(f"  [cyan]Emails:[/cyan] {w.emails}")
        print(f"  [cyan]Name Servers:[/cyan] {w.name_servers}")
    except Exception as e:
        print(f"[red]WHOIS failed: {e}[/red]")

    try:
        print(f"[bold green]DNS Records:[/bold green]")
        for record in ["A", "MX", "NS", "TXT"]:
            answers = dns.resolver.resolve(domain, record, raise_on_no_answer=False)
            for rdata in answers:
                print(f"[cyan]{record}:[/cyan] {rdata}")
    except Exception as e:
        print(f"[red]DNS Records failed: {e}[/red]")

def main(args=None):
    if not args:
        print("[dryad] Usage: dryad <target-domain>")
        return
    print(f"[dryad] Recon against: {args[0]}")

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
