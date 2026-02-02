from datetime import datetime

class Orchestrator:
    def __init__(self, router, planner, executor, memory, recall):
        self.router = router
        self.planner = planner
        self.executor = executor
        self.memory = memory
        self.recall = recall

    def run(self, user_goal: str):
        print("\n🧠 Orchestrator started")
        print(f"🎯 Goal: {user_goal}")

        # 1. Route task
        decision = self.router.route(user_goal)
        print(f"➡ Routed to: {decision}")

        # 2. Create plan
        plan = self.planner.create_plan(user_goal)
        print("\n📋 Execution Plan:")
        for i, step in enumerate(plan["plan"], 1):
            print(f"{i}. {step['step']} → {step['agent']}")

        # 3. Execute plan
        print("\n⚙️ Executing plan...")
        results = self.executor.execute(plan["plan"])

        # 4. Save memory
        self.memory.save(
            event_type="orchestrated_run",
            content={
                "goal": user_goal,
                "results": results,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

        # 5. Recall memory
        past = self.recall.search("orchestrated_run")

        print("\n🧠 Past runs found:", len(past))
        print("✅ Orchestration complete")

        return results