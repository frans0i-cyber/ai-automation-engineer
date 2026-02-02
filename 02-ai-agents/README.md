# 🤖 AI Agents

This module contains **agent-based AI systems** that demonstrate
decision-making, planning, and tool usage using LLMs.

These agents build on the automation foundation and focus on
**reasoning + orchestration**, not just single prompts.

---

## 📂 Agents in this module

### 01️⃣ Task Router Agent
Routes a user task to the most appropriate specialized agent using structured JSON output.

**Skills shown:**
- LLM-based decision routing
- Strict JSON validation
- Agent orchestration

📁 `01-task-router-agent`

---

### 02️⃣ Tool-Using Agent
Selects and executes the correct tool (calendar, email, notes) based on user intent.

**Skills shown:**
- Tool selection via LLM
- Action + arguments extraction
- Safe tool execution

📁 `02-tool-using-agent`

---

### 03️⃣ Planner Agent
Breaks down a high-level goal into a structured, multi-step execution plan with assigned agents.

**Skills shown:**
- Multi-step planning
- Agent delegation
- Structured planning output

📁 `03-planner-agent`

---

### 04️⃣ Executor Agent
Executes structured plans produced by the Planner Agent by dispatching tasks
to specialized assistants (email, calendar, notes, etc.).

📁 `04-executor-agent`

---

### 05️⃣ Memory Agent
**Purpose:**  
Persists structured information from agent executions for future use.

**Key Concepts:**
- Long-term memory
- Event-based storage
- Timestamped records
- Deterministic data handling

📁 `05-memory-agent`

---

### 06️⃣ Memory Recall Agent
**Purpose:**  
Retrieves previously stored structured memories from shared persistent storage and exposes them to other agents for context-aware execution.

**Key Concepts:**
- Memory retrieval
- Event-type filtering
- Shared state across agents
- Stateless agent, stateful storage

📁 `06-memory-recall-agent`

---

## 🎯 Goal
Demonstrate **real-world agent patterns** used in modern AI systems:


routing → planning → execution → tools.

