import os
import subprocess

REAL_HOME = os.path.expanduser("~")
FAKE_LAYER = os.path.join(REAL_HOME, ".lune_shadow")

def create_fake_layer():
    os.makedirs(FAKE_LAYER, exist_ok=True)
    decoy_files = {
        "cmd_history.txt": "nmap -A internal_net\nmsfconsole\npython3 ransom.py",
        "wallet_seed.png": "ThisIsFakeBase64==",
        "api_keys_leaked.json": '{"key":"sk_live_fake"}',
        "ssh_logs.log": "Accepted password for root from 192.168.99.99 port 22"
    }
    for fname, content in decoy_files.items():
        with open(os.path.join(FAKE_LAYER, fname), "w") as f:
            f.write(content)
    print("[+] Fake layer initialized at", FAKE_LAYER)

def mount_fake_view():
    os.system(f"sudo mount --bind {FAKE_LAYER} {REAL_HOME}/Documents")
    print("[+] Traitor mode activated — hallucinated system view live.")

def unmount_fake_view():
    os.system(f"sudo umount {REAL_HOME}/Documents")
    print("[+] Reality restored — true system view visible.")

def main():
    mode = os.environ.get("LUNE_MODE", "real")
    if mode == "fake":
        mount_fake_view()
    else:
        unmount_fake_view()

if __name__ == "__main__":
    create_fake_layer()
    main()
