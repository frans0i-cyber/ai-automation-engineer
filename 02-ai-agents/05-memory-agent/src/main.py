from memory import MemoryStore

def main():
    memory = MemoryStore()

    # Simulate storing execution results
    memory.save("email_summary", {
        "count": 5,
        "urgent": 2
    })

    memory.save("calendar_event", {
        "title": "Team Sync",
        "time": "Tomorrow 3PM"
    })

    print("📚 Stored Memories:")
    for item in memory.search("email_summary"):
        print(item)


if __name__ == "__main__":
    main()