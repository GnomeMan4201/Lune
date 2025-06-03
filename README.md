# LUNE :: Offensive Operator Console
![Build Status](https://github.com/GnomeMan4201/Lune/actions/workflows/test.yml/badge.svg)
![Docs Status](https://github.com/GnomeMan4201/Lune/actions/workflows/deploy_docs.yml/badge.svg)


A terminal-based shell interface for secure operator workflows, module execution, and auditing. Designed for elegance, usability, and stealth.

---

##  Features

-  PIN-protected access
-  Audit logging of all command usage
- Custom modules (intelshare, cleanroom, traitor, injector)
- System stats (CPU, RAM, OS)
-  Config-based PIN control via `~/.luneconfig`

---

##  Folder Structure

```
LUNE/
├── lune-ui.py           # Main launcher script
├── startup/             # Drop-in modules with `main()` entrypoints
│   ├── intelshare.py
│   ├── cleanroom.py
│   ├── traitor.py
│   └── injector.py
└── utils/
    └── security.py      # PIN & audit logic (uses config)
```

---

##  Requirements

- Python 3.7+
- Packages: `psutil`

Install with:
```bash
pip install psutil
```

---

##  Configuring Your PIN

Create a hidden config file in your home directory:

```ini
# ~/.luneconfig
[auth]
pin = 42069
```

Change the PIN to anything you like. This replaces hardcoded values.

---

##  Usage

Start the shell:
```bash
python3 lune-ui.py
```

Then interact:
```
> list        # Show available modules
> run intelshare
> auditlog    # View recent audit entries
> sysinfo     # View system information
> exit        # Quit the interface
```

---

##  Writing Your Own Modules

Each module should be placed in `startup/` and contain a `main()` function:

```python
# startup/ghostctl.py
def main():
    print("[ghostctl] Executed ghost control module.")
```

Once dropped in, it's callable via:
```bash
> run ghostctl
```

---

##  Tips

- `Ctrl+C` exits safely
- All access is logged to `~/.lune_audit.log`
- UI color & layout can be themed further

---

##  Credits

Designed for top-tier operator workflows by LUNE. Feedback and feature requests welcome.
