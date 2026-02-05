# System Architecture Diagram

```mermaid
flowchart TD
    User["User / CLI Input"] --> CLI["CLI Runner (09_cli_runner)"]

    CLI --> Router["Task Router Agent"]
    Router --> Planner["Planner Agent"]

    Planner --> Executor["Executor Agent"]

    Executor --> ToolEmail["Email Tool / Assistant"]
    Executor --> ToolCalendar["Calendar Tool / Assistant"]
    Executor --> ToolNotes["Notes / Document Tool"]

    Executor --> Memory["Memory Agent"]
    Memory --> Recall["Memory Recall Agent"]

    Recall --> Executor

    subgraph Registry
        AgentRegistry["Agent Registry"]
    end

    Router --> AgentRegistry
    Planner --> AgentRegistry
    Executor --> AgentRegistry
