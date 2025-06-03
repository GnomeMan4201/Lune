import http.server
import socketserver
import threading
import time
import random
import string
from pathlib import Path
from rich import print, box
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

HOST = "0.0.0.0"
PORT = 8081

def generate_slug(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def serve_file(file_path, slug, expire_after=None):
    class PayloadHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path.strip("/") != slug:
                self.send_error(404)
                return
            self.send_response(200)
            self.send_header("Content-type", "application/octet-stream")
            self.end_headers()
            with open(file_path, "rb") as f:
                self.wfile.write(f.read())
            print(f"[dim]{time.strftime('%H:%M:%S')}[/dim] [cyan]Payload served to:[/cyan] {self.client_address[0]}")

    handler = PayloadHandler
    httpd = socketserver.TCPServer((HOST, PORT), handler)

    def expire_timer():
        time.sleep(expire_after)
        print("[red]Timer expired. Shutting down server.[/red]")
        httpd.shutdown()

    if expire_after:
        threading.Thread(target=expire_timer, daemon=True).start()

    print(f"[bold green]Hosting:[/bold green] http://{HOST}:{PORT}/{slug}")
    print("[dim]Ctrl+C to stop[/dim]")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[red]Server stopped by user.[/red]")
        httpd.shutdown()

def run():
    print(Panel("📦 [bold magenta]PALEBOX — Remote Payload Stager[/bold magenta]", box=box.ROUNDED))

    file_path = Prompt.ask("[yellow]Enter path to payload file[/yellow]").strip()
    if not Path(file_path).is_file():
        print("[red]Invalid file path[/red]")
        return

    slug = generate_slug()
    try:
        exp = Prompt.ask("[cyan]Expire after how many seconds? (0 = never)[/cyan]", default="0")
        expire_after = int(exp) if int(exp) > 0 else None
    except:
        expire_after = None

    serve_file(file_path, slug, expire_after)

def main(args=None):
    print("[palebox] 🎁 Payload stager box ready.")
    print("Use: palebox <payload>.py")

if __name__ == "__main__":
    main()
