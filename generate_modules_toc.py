import os

GENERATED_DIR = "docs/generated"
OUTPUT_RST = "docs/modules.rst"

# Read and sort .rst filenames
rst_files = sorted(
    f for f in os.listdir(GENERATED_DIR)
    if f.endswith(".rst")
)

# Create toctree entries
toc_entries = [
    f"   generated/{f[:-4]}"  # Remove .rst extension
    for f in rst_files
]

# Compose full .rst content
content = """Modules
=======

.. toctree::
   :maxdepth: 2
   :caption: Module Index

"""

content += "\n".join(toc_entries) + "\n"

# Write to file
with open(OUTPUT_RST, "w") as f:
    f.write(content)

print(f"[✓] Updated {OUTPUT_RST} with {len(toc_entries)} entries.")
