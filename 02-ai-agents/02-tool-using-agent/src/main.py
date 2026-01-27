from agent import decide_tool

TOOLS = {
    "calendar": {
        "create_event": lambda args: print(f"📅 Creating event: {args}"),
        "list_events": lambda args: print("📅 Listing events"),
    },
    "email": {
        "send_email": lambda args: print(f"📧 Sending email: {args}"),
        "summarize_email": lambda args: print("📨 Summarizing emails"),
    },
    "notes": {
        "create_note": lambda args: print(f"📝 Creating note: {args}"),
    },
}

def main():
    task = "Schedule a meeting tomorrow at 3pm"
    decision = decide_tool(task)

    tool = decision["tool"]
    action = decision["action"]
    args = decision["arguments"]

    print(f"\n🛠 Tool chosen: {tool}")
    print(f"⚙️ Action: {action}")

    TOOLS.get(tool, {}).get(
        action,
        lambda _: print("❌ Unknown tool/action")
    )(args)

if __name__ == "__main__":
    main()