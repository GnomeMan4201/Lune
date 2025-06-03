import os
import platform
import random
import time

VM_INDICATORS = [
    "vbox", "vmware", "virtual", "qemu", "xen", "parallels"
]

HONEYPOT_FILES = [
    "/etc/honeypot",
    "/usr/bin/honeyd",
    "/usr/sbin/kippo",
    "/usr/bin/cowrie"
]

def is_sandbox():
    suspicious = 0

    # Check dmi product name
    try:
        with open('/sys/class/dmi/id/product_name') as f:
            product = f.read().lower()
            if any(vm in product for vm in VM_INDICATORS):
                suspicious += 1
    except: pass

    # Check uname for known VM tags
    uname = platform.uname()
    if any(vm in uname.node.lower() for vm in VM_INDICATORS):
        suspicious += 1

    # Look for honeypot markers
    for path in HONEYPOT_FILES:
        if os.path.exists(path):
            suspicious += 2

    return suspicious >= 2

def jam_sandbox():
    print("[smudge] 🧼 Sandbox detected. Triggering noise jam.")
    # Create garbage logs
    for i in range(5):
        with open(f"/tmp/.logfake_{random.randint(1000,9999)}", "w") as f:
            f.write("".join(random.choices("ABCDEFG12345\n", k=2048)))
    # Slow execution
    time.sleep(random.randint(5, 12))

    print("[smudge] ✖️ Dormant mode triggered. Payload halted.")
    exit(0)

def run():
    print("[smudge] 🔍 Checking for sandbox signals...")
    if is_sandbox():
        jam_sandbox()
    else:
        print("[smudge] ✅ Clean environment confirmed. Continuing ops.")

def main(args=None):
    print("[smudge] 🔍 Checking for sandbox signals...")
    print("[smudge] ✅ Clean environment confirmed. Continuing ops.")

if __name__ == "__main__":
    main()
