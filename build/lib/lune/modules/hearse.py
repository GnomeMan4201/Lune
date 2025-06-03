import os
import time
from datetime import datetime

LOGFILE = "/tmp/.lune_hearse.log"

def trace_pty():
    try:
        import ptyprocess
    except ImportError:
        print("[hearse] ❌ Missing dependency: ptyprocess")
        return

    # Placeholder for live PTY scan (simulated for now)
    print("[hearse] 🔎 Starting pseudo-terminal trace...")

    sessions = []
    try:
        output = os.popen("ps aux | grep 'pts/' | grep -v grep").read()
        for line in output.strip().split('\n'):
            if line:
                parts = line.split()
                pid = parts[1]
                tty = parts[6]
                user = parts[0]
                cmd = ' '.join(parts[10:])
                sessions.append((pid, tty, user, cmd))
    except Exception as e:
        print(f"[hearse] ⚠️ Error tracing sessions: {e}")
        return

    with open(LOGFILE, "a") as log:
        for pid, tty, user, cmd in sessions:
            stamp = datetime.utcnow().isoformat()
            log.write(f"{stamp} | PID:{pid} | TTY:{tty} | USER:{user} | CMD:{cmd}\n")

    print(f"[hearse] 🧪 {len(sessions)} sessions observed. Logged to {LOGFILE}")

def run():
    print("[hearse] 🫥 Passive shell trace engaged...")
    trace_pty()

def main(args=None):
    print("[hearse] 🫥 Passive shell trace engaged...")
    try:
        import ptyprocess
    except ImportError:
        print("[hearse] ❌ Missing dependency: ptyprocess")

if __name__ == "__main__":
    main()
