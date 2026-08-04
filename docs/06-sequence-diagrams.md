```text
User

 │
 │ POST /sprint-planning
 ▼

FastAPI
 │
 ▼

Workflow Engine
 │
 ▼

Runtime Executor
 │
 ▼

Coordinator Agent
 │
 ▼

Planner Agent
 │
 ├──────────────────────────────────────────────┐
 │                                              │
 ▼                                              │
Task Generator Agent                            │
 │                                              │
 │ generate()                                   │
 ▼                                              │
Ollama                                           │
 │                                              │
 ▼                                              │
Planning Tasks                                  │
 │                                              │
 ▼                                              │
Story Point Agent                               │
 │                                              │
 ▼                                              │
Ollama                                           │
 │                                              │
 ▼                                              │
Updated Tasks                                   │
 │                                              │
 ▼                                              │
Dependency Agent                                │
 │                                              │
 ▼                                              │
Ollama                                           │
 │                                              │
 ▼                                              │
Updated Tasks                                   │
 │                                              │
 ▼                                              │
Review Agent                                    │
 │                                              │
 ▼                                              │
Ollama                                           │
 │                                              │
 ▼                                              │
Final Planning Result                           │
 │                                              │
 └──────────────────────────────────────────────┘
 │
 ▼

Workflow Memory
 │
 ▼

Publisher Agent
 │
 ▼

GitHub Publishing Service
 │
 ▼

GitHub REST API
 │
 ▼

GitHub Issues Created
 │
 ▼

Workflow Completed
 │
 ▼

HTTP 200 Response
```