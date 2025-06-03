# Lune

Lune is a modular adversary simulation and red team operations framework.  
It supports controlled offensive testing, deception operations, and post-exploitation tooling for research and training environments.

---

## Features

- Modular architecture with a growing library of payloads and deception tools
- Multiple interfaces: CLI, TUI, and GUI
- CVE emulation modules and custom post-exploitation payloads
- Ghostload, nullflow, stealth execution, and operator-focused tooling

---

## Installation

```bash
git clone https://github.com/GnomeMan4201/Lune.git
cd Lune
pip install -r requirements.txt
```

---

## Usage

Run the interactive TUI:

```bash
python -m lune.lune_tui
```

Run a specific module:

```bash
python -m lune.modules.<module_name>
```

---

## Contributing

Pull requests are welcome.  
See `CONTRIBUTING.md` for guidelines on how to contribute, report issues, or propose new modules.

---

## License

Lune is released under the MIT License.  
See `LICENSE` for more details.
