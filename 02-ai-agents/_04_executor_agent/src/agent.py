def execute_step(step: dict):
    agent = step["agent"]
    task = step["step"]

    print(f"⚙️ Executing with {agent}: {task}")

    if agent == "Email Assistant":
        return f"📧 Emails summarized"
    elif agent == "Calendar Assistant":
        return f"📅 Meeting scheduled"
    elif agent == "Note-taking Assistant":
        return f"📝 Notes created"
    else:
        return f"❌ Unknown agent: {agent}"
    
def execute_plan(plan: dict):
    results = []
    for step in plan["plan"]:
        result = execute_step(step)
        results.append({
            "step": step["step"],
            "agent": step["agent"],
            "result": result
        })
    return results