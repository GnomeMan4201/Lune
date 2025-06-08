# 🧠 Lune Design Overview

## Architecture

Lune is built using a simple beaconing-based C2 architecture:

- **Agents**: Lightweight Python scripts that beacon to a server, fetch queued tasks, and execute them.
- **Server**: A Flask application serving as a command & control center, handling task queues and result reporting.
- **Storage**: Each agent has a unique task file stored in `data/`.

## Communication Flow

1. Agent sends GET to `/api/update/<agent_id>` to fetch tasks.
2. Agent executes tasks via `os.popen`.
3. Results are sent to `/api/report` via POST.
4. Operator queues tasks to `/api/queue/<agent_id>`.

## Key Components

- `lune_agent.py`: Periodic beacon client with jitter.
- `c2.py`: Flask server for tasking and result ingestion.
- `data/`: Per-agent task storage in JSON format.

## Planned Improvements

- Encryption for agent-server traffic (AES or TLS)
- CLI-based operator frontend
- Modular task support (`modules/` directory)
- Agent authentication
- Persistent data logging
