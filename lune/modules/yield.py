"""
yield.py — Signature Drift Detector
Analyzes file headers and entropy to detect tampering or AV evasion tactics.
"""

import os
import math

def yield_main(*args):
    if not args:
        return "[yield] Usage: yield /path/to/file"

    target_file = args[0]

    if not os.path.isfile(target_file):
        return f"[yield] File not found: {target_file}"

    report = [banner(target_file)]
    report.append(check_magic(target_file))
    report.append(analyze_entropy(target_file))
    report.append(check_nulls(target_file))
    return "\n".join(report)


def banner(path):
    return f"""
╔═════════════════════════════════════╗
║  yield — signature drift analysis  ║
╠═════════════════════════════════════╣
║  File: {os.path.basename(path):<30}║
╚═════════════════════════════════════╝
"""


def check_magic(file_path):
    with open(file_path, "rb") as f:
        magic = f.read(4).hex()
        return f"[header] Magic bytes: {magic}"


def analyze_entropy(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        if not data:
            return "[entropy] File is empty."

        byte_counts = [0] * 256
        for byte in data:
            byte_counts[byte] += 1

        entropy = 0.0
        for count in byte_counts:
            if count == 0:
                continue
            p = count / len(data)
            entropy -= p * math.log2(p)

        return f"[entropy] Shannon entropy: {entropy:.2f}"


def check_nulls(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        nulls = data.count(0x00)
        ratio = nulls / len(data) if data else 0
        return f"[null-padding] Null byte ratio: {ratio:.2%}"


run = yield_main

def main(args=None):
    if not args or len(args) < 1:
        print("[yield] Usage: yield /path/to/file")
        return
    target = args[0]
    print(f"[yield] Analyzing target: {target}")

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
