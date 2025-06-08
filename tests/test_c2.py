import os
import json
from c2 import app, save_tasks, load_tasks

def test_task_queue_and_fetch():
    client = app.test_client()
    agent_id = "test_agent"

    # Queue a task
    response = client.post(f"/api/queue/{agent_id}", json={"task": "whoami"})
    assert response.status_code == 200

    # Fetch the task
    response = client.get(f"/api/update/{agent_id}")
    assert response.status_code == 200
    tasks = json.loads(response.data)
    assert tasks == ["whoami"]

    # Ensure the queue is cleared after fetch
    response = client.get(f"/api/update/{agent_id}")
    tasks = json.loads(response.data)
    assert tasks == []
