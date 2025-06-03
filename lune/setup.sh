#!/bin/bash
echo "[+] Initializing LUNE environment..."

# Create and activate venv
python3 -m venv venv
source venv/bin/activate

# Install dependencies
if [ -f "requirements.txt" ]; then
    echo "[+] Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "[!] No requirements.txt found, skipping package install."
fi

echo "[+] Setup complete. Run with:"
echo "source venv/bin/activate && python3 lune-tui.py"
