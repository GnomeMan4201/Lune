import json
import os

AGENT_FILE = "agents.json"

def load_agents():
    if not os.path.exists(AGENT_FILE):
        return {}
    with open(AGENT_FILE, "r") as f:
        return json.load(f)

def save_agents(agents):
    with open(AGENT_FILE, "w") as f:
        json.dump(agents, f, indent=2)

def register_agent(agent_id):
    agents = load_agents()
    if agent_id not in agents:
        agents[agent_id] = {"tasks": [], "last_seen": None}
        save_agents(agents)

def update_last_seen(agent_id):
    from datetime import datetime
    agents = load_agents()
    if agent_id in agents:
        agents[agent_id]["last_seen"] = datetime.utcnow().isoformat()
        save_agents(agents)
