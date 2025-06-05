import time
from scapy.all import sniff, DNSQR, IP
from rich import print
from rich.panel import Panel
from datetime import datetime

def process_packet(packet):
    if packet.haslayer(DNSQR):
        qname = packet[DNSQR].qname.decode("utf-8")
        src_ip = packet[IP].src
        timestamp = datetime.now().strftime("%H:%M:%S")

        print(f"[dim]{timestamp}[/dim] [bold cyan]{src_ip}[/bold cyan] → [green]{qname}[/green]")

def run():
    print(Panel("🌒 [bold]NOCT — DNS Watchdog & Beacon Logger[/bold]", style="bold magenta"))
    print("[bold yellow]Listening for outbound DNS traffic...[/bold yellow]")
    print("[dim]Press Ctrl+C to stop.[/dim]\n")

    try:
        sniff(filter="udp port 53", prn=process_packet, store=0)
    except PermissionError:
        print("[red]Permission denied. Try running with sudo.[/red]")
    except KeyboardInterrupt:
        print("\n[bold red]Stopped.[/bold red]")

def main(args=None):
    print("[noct] 🌙 Stealth scan mode (nocturnal ops)")

if __name__ == "__main__":
    main()
