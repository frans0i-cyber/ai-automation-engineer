from agent import execute_step

def main():
    plan = {
        "plan": [
            {"step": "Summarize unread emails", "agent": "Email Assistant"},
            {"step": "Schedule meetings", "agent": "Calendar Assistant"},
            {"step": "Create daily notes", "agent": "Note-taking Assistant"},
        ]
    }

    for i, step in enumerate(plan["plan"], 1):
        result = execute_step(step)
        print(f"{i}. Result: {result}")

if __name__ == "__main__":
    main()