from agent import create_plan

def main():
    goal = "Prepare my workday: summarize emails, schedule meetings, and create notes"
    plan = create_plan(goal)

    for i, step in enumerate(plan["plan"], 1):
        print(f"{i}. {step['step']} -> {step['agent']}")

if __name__ == "__main__":
    main()