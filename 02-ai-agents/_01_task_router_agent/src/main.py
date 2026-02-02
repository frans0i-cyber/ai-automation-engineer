from agent import route_task

AGENTS = {
    "email_summarizer": lambda t: print("📧 Email Summarizer handling:", t),
    "calendar_agent": lambda t: print("📅 Calendar Agent handling:", t),
}

def main():
    task = "Summarize my unread emails"
    decision = route_task(task)

    agent = decision["chosen_agent"]
    handler = AGENTS.get(agent)

    if handler:
        handler(task)
    else:
        print("❌ Unknown agent:", agent)

if __name__ == "__main__":
    main()