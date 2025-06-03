import os
import readline
from xattr_tagging import check_tag

PROMPT = "lune> "

def highlight_file(filename):
    status = check_tag(filename)
    if status == "fake":
        return f"🟥 {filename}"
    elif status == "real":
        return f"🟩 {filename}"
    else:
        return f"⬜ {filename}"

def list_dir(path="."):
    try:
        files = os.listdir(path)
        for file in files:
            print(highlight_file(file))
    except Exception as e:
        print(f"[!] Error listing directory: {e}")

def start_shell():
    print("🌘 Operator Lens Shell — See what they cannot.\nType 'ls' to list hallucinated vs real files.\nType 'exit' to quit.\n")
    while True:
        try:
            cmd = input(PROMPT).strip()
            if cmd == "exit":
                break
            elif cmd == "ls":
                list_dir()
            elif cmd.startswith("cd "):
                path = cmd[3:].strip()
                os.chdir(path)
            else:
                os.system(cmd)
        except KeyboardInterrupt:
            print("\n[!] Interrupted.")
            break
        except Exception as e:
            print(f"[!] Error: {e}")

if __name__ == "__main__":
    start_shell()
