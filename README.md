# 🌙 Lune

**Lune** is a modular adversary simulation and red team operations framework. It enables the deployment of customizable agents across systems, simulating command-and-control (C2) behavior for educational, research, and internal testing purposes.

---

## 🧠 Key Features

- **Agent-Server Communication** via HTTP
- **Beaconing Model** with task polling and result delivery
- **Task Queuing System** with JSON-based storage
- **Modular Command Execution** via agent scripts
- **Jitter Injection** to simulate stealth
- **Pluggable Design** for easy module expansion

---

## 🚀 Getting Started

### 1. Start the C2 Server

```bash
python3 c2.py
```

### 2. Deploy an Agent

```bash
python3 agents/lune_agent.py
```

### 3. Queue Tasks to Agent

Use a tool like `curl` or Postman to send tasks:

```bash
curl -X POST -H "Content-Type: application/json" \
    -d '{"task": "whoami"}' \
    http://localhost:5000/api/queue/agent_001
```

---

## 🛠 Project Structure

```
Lune/
├── agents/            # Agent implementations
│   └── lune_agent.py
├── c2.py              # Flask-based command & control server
├── data/              # Stores agent task files (JSON)
├── docs/              # Design documents
├── tests/             # Unit and integration tests
└── README.md
```

---

## 📐 Architecture

```plaintext
[ Operator ] <--[HTTP]--> [ Flask C2 Server ]
                                 |
                +-----------------------------+
                | Agent ID: agent_001         |
                |                             |
         [Agent: lune_agent.py] <--- Beacon Poll
                |                             |
        Executes commands via os.popen()      |
        Sends results to /api/report          |
```

---

## ⚖️ Disclaimer

Lune is for **educational and research purposes only**. Use responsibly.
