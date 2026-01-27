# 🛠️ Tool-Using AI Agent

A lightweight AI agent that **selects and executes the correct tool** based on a user’s task using **Google Gemini** and **structured JSON outputs**.

This project demonstrates a core capability of modern AI agents:  
**LLM-powered tool selection + deterministic execution**.

---

## 🚀 What This Agent Does

Given a natural language task like:

> “Schedule a meeting tomorrow at 3pm”

The agent will:

1. Analyze the task using an LLM
2. Choose the **correct tool** (calendar, email, notes, etc.)
3. Select the correct **action**
4. Return **strict JSON**
5. Execute the tool automatically

---

## 🧠 Available Tools

- **Calendar**
  - `create_event`
  - `list_events`
- **Email**
  - `send_email`
  - `summarize_email`
- **Notes**
  - `create_note`

---

## 🏗️ Architecture