import os
from datetime import datetime

def generate_fake_keys():
    traps = {
        "AWS_SECRET_ACCESS_KEY": "fake123EXAMPLEKEYDOESNOTWORKabc456",
        "STRIPE_KEY": "sk_test_fake_4eC39HqLyjWDarjtT1zdp7dc",
        "GOOGLE_API_KEY": "AIzaSyFAKEFAKEFAKE123abc"
    }
    with open("config/fake.env", "w") as f:
        for key, value in traps.items():
            f.write(f"{key}={value}\n")
    print("[+] Fake secrets generated in config/fake.env")

if __name__ == "__main__":
    os.makedirs("config", exist_ok=True)
    generate_fake_keys()
