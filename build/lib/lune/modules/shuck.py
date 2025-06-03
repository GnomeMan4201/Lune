# shuck.py — Encrypted Payload Dropper
import base64
import os
from rich import print, panel

DROPPED_PATH = "/tmp/.shucked_payload.sh"
ENCRYPTED_B64 = "IyEvYmluL2Jhc2gKZWNobyAiU3VjY2Vzc2Z1bGx5IGRyb3BwZWQgcGF5bG9hZCEi"

def decode_and_drop(payload_b64, out_path):
    try:
        decoded = base64.b64decode(payload_b64.encode()).decode()
        with open(out_path, "w") as f:
            f.write(decoded)
        os.chmod(out_path, 0o755)
        print(f"[green]Payload dropped and decoded:[/green] {out_path}")
    except Exception as e:
        print(f"[red]Shuck failure:[/red] {e}")

def run():
    print(panel.Panel("🌰 [bold yellow]SHUCK[/bold yellow] — Decrypt and Drop Payload"))
    decode_and_drop(ENCRYPTED_B64, DROPPED_PATH)


main = run
