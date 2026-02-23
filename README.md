# 🧠 AI Automation Engineer Lab

A modular, production-style multi-agent AI system built to demonstrate
real-world AI automation architecture — not just prompt demos.

---

## 🚀 What This Project Is

This repository implements a scalable AI system with:

- Task routing
- Multi-step planning
- Deterministic execution
- Persistent memory
- Context recall
- Agent orchestration
- Workflow automation readiness (n8n)

It mirrors how modern AI automation systems are designed inside companies.

---

## 🏗️ System Architecture

High-level flow:

User → CLI → Router → Planner → Executor → Memory → Recall → Output

📐 Full architecture breakdown:
👉 [`docs/01-architecture-overview`](docs/01-architecture-overview)

📊 Architecture diagram:
👉 [`docs/architecture/architecture-diagram.md`](docs/architecture/architecture-diagram.md)

---

## 🖥️ How To Run

```bash
cd _09_cli_runner
python run.py "Prepare my workday"
