# 🧠 Task Router AI Agent

A lightweight AI agent that **analyzes a user task and routes it to the most appropriate specialized agent** using Google Gemini.

This project demonstrates **agent decision-making, structured LLM output, and dynamic task routing** — a core pattern in modern AI agent systems.

---

## 🚀 What This Agent Does

Given a task like:

> "Summarize my unread emails"

The router agent:
1. Sends the task to an LLM with a strict routing prompt
2. Receives **structured JSON**
3. Selects the correct downstream agent
4. Executes that agent automatically

---

## 🧩 Architecture