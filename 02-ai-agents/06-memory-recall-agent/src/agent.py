import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

MEMORY_FILE = os.getenv("MEMORY_FILE", "memory.json")

def recall_memory(limit: int = 5):
    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        memories = json.load(f)

    # Sort by timestamp (newest first)
    memories = sorted(
        memories,
        key=lambda x: x.get("timestamp", ""),
        reverse=True
    )

    return memories[:limit]