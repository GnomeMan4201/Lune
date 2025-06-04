import os
import readline

FAKE_MARKERS = ["suspicious", "leaked", "backup", "cmd_exec", "wallet", "dump"]

def is_fake(filename):
    return any(marker in filename for marker in FAKE_MARKERS)

def colorize(files):
    for f in files:
        if is_fake(f):
            print(f"\033[91m🟥 {f}\033[0m")
        else:
            print(f"\033[92m🟩 {f}\033[0m")

def overlay_ls():
    files = os.listdir(".")
    colorize(sorted(files))

def overlay_shell():
    print("[overlay_shell] Starting Operator Filter Lens")
    while True:
        try:
            cmd = input("⊚ ")
            if cmd.strip() == "ls":
                overlay_ls()
            elif cmd.strip() == "exit":
                break
            else:
                os.system(cmd)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    overlay_shell()
