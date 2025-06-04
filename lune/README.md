<p align="center">
  <img src="lune/assets/lune-banner.png" alt="LUNE Banner" width="500"/>
</p>

#

LUNE (Layered Uncertainty & Network Entrapment) is a modular red team simulation and deception framework.  
It’s designed to weaponize noise, simulate phantom presence, poison logs, and sow uncertainty throughout target systems.

---

## Features

- Modular deception payload system
- System noise and log manipulation modules
- Operator presence simulation
- Phantom clipboard/data injection
- Shell alias and history poisoners
- Covert tagging and context manipulation
- TUI/CLI interface for modular ops
- Modular build and deployment pipeline

---
<p align="center">
  <img src="lune/assets/lune_github_picture.png" alt="LUNE In Use" width="800"/>
</p>
---

## Getting Started

Clone the repo and run setup:

```bash
git clone https://github.com/GnomeMan4201/Lune.git
cd Lune
chmod +x setup.sh
./setup.sh
source lune_env/bin/activate
python3 -m lune.lune_tui
