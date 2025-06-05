import json
import random
from datetime import datetime

def load_decoys(path="decoys.json"):
    with open(path) as f:
        return json.load(f)

def inject_signal(decoys, count=5):
    selected = random.sample(decoys, min(count, len(decoys)))
    for decoy in selected:
        print(f"[{datetime.now()}] Injecting decoy: {decoy}")

if __name__ == "__main__":
    decoys = load_decoys()
    inject_signal(decoys)
