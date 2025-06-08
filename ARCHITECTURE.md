# Lune Architecture Overview

This document provides a high-level overview of the architecture and data flow of the Lune adversary simulation framework.

## Components

1. **Command & Control (C2) Server**
   - Flask-based HTTP server
   - Endpoints:
     - \`/api/update/<agent_id>\`
     - \`/api/queue/<agent_id>\`
     - \`/api/result/<agent_id>\`

2. **Agent**
   - Python script (\`lune_agent.py\`)
   - Polls the server, executes tasks, sends results

3. **Task Storage**
   - JSON per-agent in the \`data/\` directory

## Data Flow

Operator ──POST──▶ C2 Server ──GET──▶ Agent  
Agent ──execute──▶ Shell ──POST──▶ C2 Server (result)

## Endpoints

| Endpoint                | Method | Purpose                  |
|-------------------------|--------|--------------------------|
| /api/update/<agent_id>  | GET    | Agent fetches tasks      |
| /api/queue/<agent_id>   | POST   | Operator submits task    |
| /api/result/<agent_id>  | POST   | Agent sends back result  |

## Design Highlights

- JSON as a lightweight task format
- Beaconing model with jitter for evasive behavior
- Modular architecture (agent/server decoupled)

## Future Extensions

- WebSocket or long-polling support
- TLS or AES encryption
- CLI or dashboard-based multi-agent control
