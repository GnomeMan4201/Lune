#!/usr/bin/env python3
import sys
import time
from datetime import datetime

RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"
RESET  = "\033[0m"
BOLD   = "\033[1m"

def banner(title):
    print(f"{RED}{BOLD}")
    print("┌─────────────────────────────────────────────┐")
    print(f"│        {title.center(37)}        │")
    print("└─────────────────────────────────────────────┘")
    print(RESET)

def print_status(message, status="+", color=GREEN):
    symbols = {
        "+": f"{color}[+]{RESET}",
        "!": f"{YELLOW}[!]{RESET}",
        "-": f"{RED}[-]{RESET}",
        "✓": f"{GREEN}[✓]{RESET}",
        "✗": f"{RED}[✗]{RESET}"
    }
    print(f"{symbols.get(status, '[ ]')} {message}")

def slow_type(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def log_event(message):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"{BLUE}[{now}]{RESET} {message}")

def prompt_menu(options):
    print()
    for i, item in enumerate(options, 1):
        print(f"{CYAN}{i}.{RESET} {item}")
    try:
        return int(input(f"\n{WHITE}Select an option:{RESET} "))
    except:
        return -1
