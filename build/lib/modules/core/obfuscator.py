import os
import random
from modules.core import tags

JUNK_CONTENTS = [
    "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDg... user@fakehost",
    "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFake... test@decoy",
    "putty-private-key-file-version: 2\nEncryption: none\nComment: junk",
    "PRIVATE KEY\nMIICeAIBADANBgkqhkiG9w0BAQEFAASCAmIwggJeAgEAAoGBALf..."
]

def obfuscate_real_file(real_path):
    dir_path = os.path.dirname(real_path)
    base_name = os.path.basename(real_path)
    obfuscated_dir = os.path.join(dir_path, "obfuscated_" + base_name)
    os.makedirs(obfuscated_dir, exist_ok=True)

    # Move real file into noisy dir
    real_target = os.path.join(obfuscated_dir, f"note_{random.randint(10,99)}.txt")
    os.rename(real_path, real_target)
    tags.tag_real(real_target)

    # Add junk files
    for i in range(10):
        junk_name = f"note_{random.randint(100,999)}.txt"
        with open(os.path.join(obfuscated_dir, junk_name), "w") as f:
            f.write(random.choice(JUNK_CONTENTS))
        tags.tag_fake(os.path.join(obfuscated_dir, junk_name))

    print(f"[+] Real file obfuscated into: {obfuscated_dir}")
