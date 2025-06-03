#!/bin/bash
gcc -fPIC -shared -o parasite.so parasite_stub.c -lpthread
echo "[+] Built parasite.so"
