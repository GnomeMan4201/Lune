#!/usr/bin/env python3
"""
update_module_index.py — Generate MODULE_INDEX.md from module_descriptions.json
"""

import json
from pathlib import Path

DESC_JSON = Path("lune/module_descriptions.json")
OUTPUT_MD = Path("MODULE_INDEX.md")

def load_descriptions():
    if not DESC_JSON.exists():
        raise FileNotFoundError(f"{DESC_JSON} not found")

    with DESC_JSON.open("r") as f:
        return json.load(f)

def write_index(descriptions):
    header = "# 🧩 Module Index\n\n| Module | Description |\n|--------|-------------|"
    lines = []

    for module, desc in sorted(descriptions.items()):
        # Skip private modules
        if module.startswith("__"):
            continue
        # Markdown-safe fallback
        desc_clean = desc if desc and "No description available." not in desc else "*Undocumented module*"
        lines.append(f"| `{module}` | {desc_clean} |")

    full_doc = header + "\n" + "\n".join(lines)
    OUTPUT_MD.write_text(full_doc, encoding="utf-8")
    print(f"[✓] Regenerated {OUTPUT_MD.name} with {len(lines)} modules.")

if __name__ == "__main__":
    try:
        descriptions = load_descriptions()
        write_index(descriptions)
    except Exception as e:
        print(f"[!] Error: {e}")
