# 🐚 LUNE Framework

**A modular, stealth-centric offensive security suite built for post-exploitation workflows, sandbox-aware payloads, signal-based exfiltration, and evasive behavior.**

LUNE is not a C2. It's not a RAT. It's a cold, adaptable toolset designed to run hard and leave no trace.

---

## 🧬 Highlights

- 30 Unique Operator-Grade Modules
- Sandbox/VM Awareness & Jammer
- Orchestrator for Custom Execution Chains
- Built-in Self-Healing + Anti-IOC Module
- Extensible Module Structure
- Zero External Noise or Sketchy Dependencies

---

## 🧩 Modules

| Category         | Modules |
|------------------|---------|
| 🧠 Recon / Signal | `spindle`, `glassing`, `mirador`, `palebox` |
| 🐾 Tracers       | `hearse`, `brine`, `shuck`, `dreamtether` |
| 🕳️ Persistence   | `relic`, `latch`, `noct`, `vane`, `yield` |
| 📡 Exfil / Payload | `siphon`, `fracture`, `cloak`, `glint`, `alibi` |
| 🔍 Evasion       | `smudge`, `dryad`, `etch`, `winnow`, `nullflow` |
| 🧰 Utility       | `velvetroom`, `fable`, `wire`, `wallflower`, `crux` |

_All modules come with self-contained `run()` methods and docstrings for usage inside the TUI._

---

## 🧪 Requirements

- Python 3.9+
- Linux or WSL/Debian preferred
- Optional: Docker (prebuilt image coming soon)

Install deps:
```bash
pip install -r requirements.txt
