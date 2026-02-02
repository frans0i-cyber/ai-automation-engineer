import sys
import os

sys.path.append(os.path.abspath("../shared_memory"))

from memory_store import MemoryStore

def main():
    memory = MemoryStore()
    memory.save(
        event_type="email_summary",
        content={
            "count": 5,
            "urgent": 2
        }
    )
    print("🧠 Memory saved successfully")

if __name__ == "__main__":
    main()