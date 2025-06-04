# veil.py — Signature Obfuscation & Output Encoder
import base64
import random
import string
from rich import print, panel

def obfuscate(code):
    encoded = base64.b64encode(code.encode()).decode()
    stub = f"import base64\nexec(base64.b64decode('{encoded}'))"
    return stub

def randomize_var_names(code):
    var_map = {}
    for var in set(filter(str.isidentifier, code.split())):
        if var.startswith('__') or len(var) < 3:
            continue
        var_map[var] = ''.join(random.choices(string.ascii_letters, k=6))
    for old, new in var_map.items():
        code = code.replace(old, new)
    return code

def run():
    print(panel.Panel("\U0001F52E [bold magenta]VEIL[/bold magenta] — Encode, Obfuscate, Confuse"))
    code = input("Paste payload or module code: ").strip()
    obf_code = randomize_var_names(code)
    final = obfuscate(obf_code)
    print("\n[green]Obfuscated Output:[/green]\n")
    print(final)