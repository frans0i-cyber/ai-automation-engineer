# 🤖 AI Agents

This section contains agent-based AI systems that demonstrate **decision-making, routing, orchestration, and tool usage** using Large Language Models.

Each subfolder is a self-contained agent project.

---

## 📂 Projects

### 01-task-router-agent
A Gemini-powered router agent that analyzes a user task and selects the most appropriate downstream agent using structured JSON output.

**Concepts covered:**
- Agent routing
- Structured LLM responses
- Confidence-based decisions
- Modular agent design

### 02-Tool-Using Agent
An AI agent that selects and executes tools based on user intent.

**Supported tools**
- Calendar (create/list events)
- Email (send/summarize)
- Notes (create)

**Pattern**
User task → LLM → Structured JSON → Tool execution

---

## 🧠 Why Agents Matter
Agent systems are a core building block of modern AI automation:
- Task delegation
- Tool selection
- Multi-agent workflows
- Autonomous decision-making

This folder documents my progression from **single-agent logic** to **multi-agent orchestration**.
