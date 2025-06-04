import os
from modules.core import tags

def color_text(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "reset": "\033[0m"
    }
    return f"{colors.get(color, '')}{text}{colors['reset']}"

def list_directory(path="."):
    try:
        for f in os.listdir(path):
            full = os.path.join(path, f)
            if os.path.isfile(full):
                if tags.is_fake(full):
                    print(color_text(f"🟥 {f}", "red"))
                elif tags.is_real(full):
                    print(color_text(f"🟩 {f}", "green"))
                else:
                    print(f"⬜ {f}")
            else:
                print(f"📁 {f}/")
    except Exception as e:
        print(f"[!] Error reading directory: {e}")
