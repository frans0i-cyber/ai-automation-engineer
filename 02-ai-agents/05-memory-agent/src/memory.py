import json
import os
from datetime import datetime

MEMORY_FILE = "memory.json"


class MemoryStore:
    def __init__(self):
        if not os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "w") as f:
                json.dump([], f)

    def save(self, event_type: str, content: dict):
        memory = self._load()
        memory.append({
            "timestamp": datetime.utcnow().isoformat(),
            "type": event_type,
            "content": content
        })
        self._save(memory)

    def search(self, event_type: str):
        memory = self._load()
        return [m for m in memory if m["type"] == event_type]

    def _load(self):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    def _save(self, memory):
        with open(MEMORY_FILE, "w") as f:
            json.dump(memory, f, indent=2)