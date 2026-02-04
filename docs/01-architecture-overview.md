# 🧠 System Architecture Overview

## Why this architecture exists

This repository is not a collection of isolated scripts.
It is a modular AI automation system designed to mirror
real-world production patterns.

The goal is to move beyond:
- single-prompt demos
- hard-coded logic
- stateless executions

And instead implement:
- routing
- planning
- execution
- memory
- orchestration

## High-Level Flow

User / Trigger
   ↓
Task Router Agent
   ↓
Planner Agent
   ↓
Executor Agent
   ↓
Memory Store ↔ Memory Recall
   ↓
Orchestrator Agent

***mermaid diagram HERE***

## Core Subsystems

### 1. AI Agents (`02-ai-agents`)
Contains all reasoning and decision-making agents:
- Router
- Planner
- Executor
- Memory
- Orchestrator
- Agent Registry

Each agent follows a single-responsibility design.

### 2. Automation Layer (`03-n8n-workflows`)
This layer connects the AI system to real-world triggers.

Examples:
- Email received
- Cron schedules
- Webhooks
- Manual triggers

n8n acts as the orchestration *entry point*,
while AI agents handle reasoning and execution.

### 3. LLM Integrations (`04-llm-integrations`)
Abstraction layer for interacting with LLM providers.

Purpose:
- Avoid vendor lock-in
- Standardize prompt + response handling
- Support local or hosted models

## Design Principles

- Separation of concerns
- Deterministic execution
- Replaceable components
- Automation-first mindset

## Why this matters

This architecture mirrors how modern AI systems are built
inside real companies:

AI ≠ a chatbot  
AI = a component inside an automation pipeline