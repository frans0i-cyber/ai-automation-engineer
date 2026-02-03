import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

from _07_orchestrator_agent.src.main import main as orchestrate


def cli():
    if len(sys.argv) < 2:
        print("❌ Usage: python run.py \"Your task here\"")
        sys.exit(1)

    task = sys.argv[1]
    print(f"🚀 Running AI Automation System")
    print(f"📝 Task: {task}\n")

    orchestrate(task)


if __name__ == "__main__":
    cli()