import os
import argparse
import subprocess
from pathlib import Path

def tag_file(file_path, tag):
    try:
        subprocess.run(["xattr", "-w", "user.trust", tag, file_path], check=True)
        print(f"[+] Tagged {file_path} as {tag}")
    except subprocess.CalledProcessError as e:
        print(f"[!] Failed to tag {file_path}: {e}")

def scan_dir(directory):
    print("\n🔍 Covert Tag Scanner Report\n")
    for file in sorted(Path(directory).glob("*")):
        try:
            output = subprocess.check_output(["xattr", file])
            if b"user.trust" in output:
                tag = subprocess.check_output(["xattr", "-p", "user.trust", file])
                print(f"{file.name}: {tag.decode().strip()}")
            else:
                print(f"{file.name}: untagged")
        except subprocess.CalledProcessError:
            print(f"{file.name}: untagged")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tag", help="Tag file as real/fake")
    parser.add_argument("--file", help="Path to file to tag")
    parser.add_argument("--scan", help="Directory to scan")
    args = parser.parse_args()

    if args.tag and args.file:
        tag_file(args.file, args.tag)
    elif args.scan:
        scan_dir(args.scan)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
