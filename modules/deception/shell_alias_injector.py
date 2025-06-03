import os
import subprocess

# Define fake artifacts and their tags
FAKE_ARTIFACTS = {
    "malware_toolkit_v5.zip": "archive",
    "id_rsa_old": "ssh_key",
    "notes.py.old.2": "script",
    "api_keys_leaked.json": "creds",
    "wallet_seed.png": "image",
    "cmd_exec_history.txt": "history"
}

# Color codes
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def inject_aliases():
    bashrc_path = os.path.expanduser("~/.bashrc")
    with open(bashrc_path, "a") as bashrc:
        bashrc.write("\n# Lune C2 Hallucination Aliases\n")
        bashrc.write("alias ls='python3 ~/.lune/ls_override.py'\n")
        bashrc.write("alias cat='python3 ~/.lune/cat_override.py'\n")
        bashrc.write("alias nano='python3 ~/.lune/nano_override.py'\n")
    print("[+] Shell aliases injected.")

def create_override_scripts():
    lune_dir = os.path.expanduser("~/.lune")
    os.makedirs(lune_dir, exist_ok=True)

    # ls_override.py
    ls_override = os.path.join(lune_dir, "ls_override.py")
    with open(ls_override, "w") as f:
        f.write("import os\n")
        f.write("FAKE_FILES = " + str(list(FAKE_ARTIFACTS.keys())) + "\n")
        f.write("RED = '\\033[91m'\n")
        f.write("GREEN = '\\033[92m'\n")
        f.write("RESET = '\\033[0m'\n")
        f.write("files = os.listdir('.')\n")
        f.write("for file in files:\n")
        f.write("    if file in FAKE_FILES:\n")
        f.write("        print(f'{RED}{file}{RESET}')\n")
        f.write("    else:\n")
        f.write("        print(f'{GREEN}{file}{RESET}')\n")

    # cat_override.py
    cat_override = os.path.join(lune_dir, "cat_override.py")
    with open(cat_override, "w") as f:
        f.write("import sys\n")
        f.write("filename = sys.argv[1] if len(sys.argv) > 1 else ''\n")
        f.write("if filename in " + str(list(FAKE_ARTIFACTS.keys())) + ":\n")
        f.write("    print('This is a fake artifact.')\n")
        f.write("else:\n")
        f.write("    with open(filename, 'r') as file:\n")
        f.write("        print(file.read())\n")

    # nano_override.py
    nano_override = os.path.join(lune_dir, "nano_override.py")
    with open(nano_override, "w") as f:
        f.write("import sys\n")
        f.write("import subprocess\n")
        f.write("filename = sys.argv[1] if len(sys.argv) > 1 else ''\n")
        f.write("subprocess.call(['nano', filename])\n")

    print("[+] Override scripts created.")

def main():
    inject_aliases()
    create_override_scripts()
    print("[+] Dynamic shell alias injection complete.")

if __name__ == "__main__":
    main()
