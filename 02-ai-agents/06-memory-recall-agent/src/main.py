import sys
import os

sys.path.append(os.path.abspath("../shared_memory"))

from memory_store import MemoryStore

def main():
    memory = MemoryStore()
    memories = memory.search()

    if not memories:
        print("🤖 No memories found.")
        return

    print("🧠 Retrieved Memories:")
    for m in memories:
        print(m)

if __name__ == "__main__":
    main()