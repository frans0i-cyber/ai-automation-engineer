from registry import AgentRegistry


def mock_planner(task):
    return f"Planning task: {task}"


def mock_executor(task):
    return f"Executing task: {task}"


def main():
    registry = AgentRegistry()

    registry.register(
        name="planner",
        capabilities=["planning", "task_breakdown"],
        handler=mock_planner
    )

    registry.register(
        name="executor",
        capabilities=["execution"],
        handler=mock_executor
    )

    print("📦 Registered agents:")
    print(registry.list_agents())

    print("\n🧠 Agents with planning capability:")
    print(registry.find_by_capability("planning"))


if __name__ == "__main__":
    main()