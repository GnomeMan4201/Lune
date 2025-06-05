#!/usr/bin/env python3
import os
import ast
import json

MODULE_DIR = "lune/modules"
output = {}

for root, _, files in os.walk(MODULE_DIR):
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)
            rel_path = os.path.relpath(path, MODULE_DIR)
            mod_name = rel_path.replace(os.sep, ".").replace(".py", "")
            with open(path, "r", encoding="utf-8") as f:
                try:
                    tree = ast.parse(f.read())
                    doc = ast.get_docstring(tree)
                    output[mod_name] = doc.strip().split("\n")[0] if doc else "No description available."
                except Exception as e:
                    output[mod_name] = f"Parse error: {e}"

with open("lune/module_descriptions.json", "w") as out:
    json.dump(output, out, indent=2)

print("[*] Updated module_descriptions.json")
