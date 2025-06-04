#!/bin/bash
# Clean script for LUNE_v1 - removes local clutter

echo "[*] Cleaning LUNE environment..."

rm -rf __pycache__/
rm -rf .lune_sessions/
rm -rf lune_env/
rm -f *.pyc
rm -f *.log
rm -f *.swp
rm -f parasite.so
rm -f lune/index.html
rm -f lune/modules/build_stub.sh

echo "[+] Clean complete."
