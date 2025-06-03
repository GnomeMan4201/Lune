
# LUNE Offensive Operator Console

**LUNE** is a modular offensive operations framework for security professionals, red teamers, and adversary simulation. It consolidates a wide array of passive, active, deception, and post-exploitation tools into a single operator-friendly shell.

---

## Features

- Text-based operator shell with interactive command set
- PIN-locked access with audit logging
- Module execution engine (`run <module>`)
- Intelligent `list` with module descriptions
- Self-diagnostic checker (`lune-check.py`)
- Modular and expandable via `startup/` directory

---

## Getting Started

### 1. Set Your PIN

LUNE uses a simple config file to control access.

```ini
~/.luneconfig
[auth]
pin = 42069
```

### 2. Run the Console

```bash
cd ~/LUNE
python3 lune-ui.py
```

### 3. Available Commands

```
list            - List all available modules
run <module>    - Execute a specific module
auditlog        - View access log
sysinfo         - View host stats
exit            - Exit the shell
```

Modules can also be run by typing their name directly:
```
lune > veil
```

---

## Adding Your Own Modules

Drop Python files into the `startup/` folder. Each must have a `main()` function. LUNE will auto-detect and load it.

---

## Checking for Issues

Run the self-diagnostic script:

```bash
python3 lune-check.py
```

To auto-fix Python package dependencies:

```bash
python3 lune-check.py --fix
```

---

## Folder Structure

```
LUNE/
├── lune-ui.py             # Entry shell interface
├── startup/               # Your custom modules
├── utils/security.py      # PIN + audit logic
└── lune-check.py          # Self-diagnostic
```

---

## License

This tool is for **educational and authorized** use only. You are responsible for your actions.

---

## Author

You.
