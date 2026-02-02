import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(BASE_DIR)

from shared_memory.memory_store import MemoryStore

from _01_task_router_agent.src.agent import route_task
from _03_planner_agent.src.agent import create_plan
from _04_executor_agent.src.agent import execute_plan
from _06_memory_recall_agent.src.agent import recall_memory


def main():
    goal = "Prepare my workday: summarize emails, schedule meetings, and create notes"

    print("🧠 Orchestrator started")
    decision = route_task(goal)

    plan = create_plan(goal)
    result = execute_plan(plan)

    memory = MemoryStore()
    memory.save("orchestration_result", result)

    recalled = recall_memory("orchestration_result")
    print("📦 Recalled Memory:", recalled)


if __name__ == "__main__":
    main()